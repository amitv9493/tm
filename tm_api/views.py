from datetime import datetime

from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from rest_framework import (
    filters,
    generics,  # noqa: F811
    status,
)
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.response import Response  # noqa: F811
from rest_framework.views import APIView  # noqa: F811
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from client.serializers import UnitSerializers as clientUnitSerializer
from equipment.models import *
from part.models import *
from project.models import *

from .paginator import CustomPagination
from .serializers import *  # noqa: F403
from .serializers import LoginSerializer


def convert_to_date(date_string: str):
    if date_string:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d").date()
        return date_obj
    else:
        return None


class EquipAndPartGeneralView(ListAPIView):
    """
    This View returns the available Parts or the Equipments
    in the given time range `start_date` and `end_date`,
    which is useful when selecting an part/equipment for a new project.

    Provide the `start_date` and `end_date`, and it will
    check if the Parts or the Equipments
    is available or not for the given date range.

    To update the a part/equip in an already created Project,
    you need to provide the `pro_id`.
    The value of the `pro_id` should be the ID
    of the project being modified.

    Query Parameters:
        - `start_date` (str): Start date of the
            time range to check for part/equip availability.
        - `end_date` (str): End date of the
            time range to check for part/equip availability.
        - `proid` (int): ID of the project to
            exclude when checking part/equip availability.
        - `warehouse` (str): Filter part/equips by warehouse location.

    Filters:
        - `serial_number` (str): Search part/equip by serial number.
        - `color_code` (str): Search part/equip by colour code.
        - `part_name` (str): Search part/equip by part name.
        - `name_of_abbreviation` (str): Search part/equip by name or abbreviation.
        - `asset_number` (str): Search part/equip by asset number.

    Pagination:
        - Uses a custom pagination class.

    Authentication:
        - JWT Authentication is required.

    Permissions:
        - Django Model Permissions and Admin User permission required.

    """

    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    model_relation_name = None
    queryset = None
    model_warehouse_field = "location_for_warehouse"

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        convert_to_date(self.request.query_params.get("end_date"))
        project_slug = self.request.query_params.get("proid", None)
        warehouse = self.request.query_params.get("warehouse", None)

        if not start_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            # equipment_prep__gt=start_date,
            equipment_delivery_tubemaster__gte=start_date,
            # equipment_prep__lt=start_date,
        )

        if project_slug:
            project_qs = project_qs.exclude(slug=project_slug)

        exclude_objects = set(
            project_qs.values_list(self.model_relation_name, flat=True)
        )

        return (
            qs.exclude(id__in=exclude_objects).order_by(
                f"{self.model_warehouse_field}__id"
            )
            if not warehouse
            else qs.exclude(id__in=exclude_objects).filter(
                **{self.model_warehouse_field: warehouse}
            )
        )


# Create your views here.

###################################################################################
#            Login API View
###################################################################################


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # email = serializer.data.get('email')
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                try:
                    user_group = (Group.objects.get(user=user.id)).name
                except Exception:
                    user_group = "None"

                token = get_tokens_for_user(user)
                return Response(
                    {
                        "token": token,
                        "msg": "Login Successful",
                        "userid": user.id,
                        "user_status": user_group,
                    },
                    status=status.HTTP_200_OK,
                )

            return Response({"errors": {"msg": -1}}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


###################################################################################
#            Unit API View
###################################################################################

from django_filters.rest_framework import DjangoFilterBackend


class UnitListView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Unit.objects.all()
    serializer_class = clientUnitSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["client"]

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid")
        client = self.request.query_params.get("client")
        project_qs = Project.objects.all()

        if start_date and end_date:
            project_qs = Project.objects.filter(
                equipment_prep__gte=start_date,
                equipment_delivery_tubemaster__lte=end_date,
            )

        if pro_id:
            project_qs = project_qs.exclude(slug=pro_id)

        unit = set(project_qs.values_list("unit", flat=True).exclude(unit=None))
        # ttd = list(ttd)

        unit_qs = qs.exclude(id__in=unit)

        return unit_qs if not client else unit_qs.filter(client=client)


###################################################################################
#            ScopeOfWork API View
###################################################################################


class ScopeOfWorkView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Scope_of_work.objects.all()
    serializer_class = SOWSerializer


###################################################################################
#            Reactor API View
###################################################################################


class ReactorView(ListAPIView):
    serializer_class = ReactorSerializer
    queryset = Reactor.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        client_id = self.request.query_params.get("client")
        unit_id = self.request.query_params.get("unit")
        qs = qs.filter(client=client_id, unit=unit_id)
        return qs


################################################################################
#                    TTD API View
################################################################################


class SwabMasterEquipmentView(EquipAndPartGeneralView):
    search_fields = [
        "serial_number",
        "pm_status",
        "alternate_name",
    ]
    queryset = SwabMaster.objects.exclude(Swab_Master_Tube_Seal_Rack__isnull=True)
    serializer_class = SwabMasterSerializer

    model_relation_name = "swabmaster_equip"


class TTDNewView(EquipAndPartGeneralView):
    serializer_class = TtdSerializer
    model_relation_name = "ttd"
    search_fields = [
        "serial_number",
        "pm_status",
        "alternate_name",
    ]

    queryset = TTD.objects.exclude(
        supply_orifice_set__isnull=True,
        pressure_sensor__isnull=True,
        TTD_tube_seal_rack__isnull=True,
    )


class TtdView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter]
    search_fields = [
        "serial_number",
        "pm_status",
        "alternate_name",
    ]
    queryset = TTD.objects.exclude(
        supply_orifice_set__isnull=True,
        pressure_sensor__isnull=True,
        TTD_tube_seal_rack__isnull=True,
    )
    queryset = TTD.objects.all()
    serializer_class = TtdSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["view_name"] = "ttdoldview"
        return context

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid")
        warehouse = self.request.query_params.get("warehouse")

        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")
        # Q()
        project_qs = Project.objects.filter(
            equipment_prep__gt=start_date,
            equipment_delivery_tubemaster__gt=end_date,
            equipment_prep__lt=end_date,
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)

        # ttd = set(j.id for i in project_qs for j in i.ttd.all())
        ttd = set(project_qs.values_list("ttd", flat=True).exclude(ttd=None))

        qs = qs.exclude(id__in=ttd).order_by("location_for_warehouse__id")

        if warehouse:
            qs = qs.filter(location_for_warehouse=warehouse)

        # print(qs.exclude(id__in=ttd).order_by("location_for_warehouse__id").count())
        # return qs.exclude(id__in=ttd).order_by("location_for_warehouse__id")
        return qs


################################################################################
#            BDD API View
################################################################################


class BddNewView(EquipAndPartGeneralView):
    queryset = BDD.objects.exclude(BDD_tube_seal_rack__isnull=True)
    serializer_class = BddSerializer
    model_relation_name = "bdd"

    search_fields = [
        "serial_number",
        "pm_status",
        "alternate_name",
    ]


class BddView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = BDD.objects.all()
    serializer_class = BddSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid")
        warehouse = self.request.query_params.get("warehouse")

        if warehouse:
            qs = qs.filter(location_for_warehouse=warehouse)
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gt=start_date,
            equipment_delivery_tubemaster__gt=end_date,
            equipment_prep__lt=end_date,
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        bdd = set()
        for i in project_qs:
            for j in i.bdd.all():
                bdd.add(j.id)

        return qs.exclude(id__in=bdd).order_by("location_for_warehouse__id")


################################################################################
#            Calibration API View
################################################################################


class CalibrationStandNewView(EquipAndPartGeneralView):
    queryset = CALIBRATION_STAND.objects.exclude(calibration_orifice_set__isnull=True)
    serializer_class = CALIBRATION_STANDSerializer
    search_fields = [
        "serial_number",
        "pm_status",
        "alternate_name",
    ]
    model_relation_name = "calibration_stand"


class CalibrationStandView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = CALIBRATION_STAND.objects.all()
    serializer_class = CALIBRATION_STANDSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid")
        warehouse = self.request.query_params.get("warehouse")

        if warehouse:
            qs = qs.filter(location_for_warehouse=warehouse)
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gt=start_date,
            equipment_delivery_tubemaster__gt=end_date,
            equipment_prep__lt=end_date,
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        calibration_stand = set()
        for i in project_qs:
            for j in i.calibration_stand.all():
                calibration_stand.add(j.id)

        return qs.exclude(id__in=calibration_stand).order_by(
            "location_for_warehouse__id"
        )


################################################################################
#                        Part API View
################################################################################


class PartNewView(EquipAndPartGeneralView):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
    ]

    model_relation_name = "part"


class PartView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Part.objects.all()
    serializer_class = PartSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid")
        # Q()
        warehouse = self.request.query_params.get("warehouse")

        if warehouse:
            qs = qs.filter(location_for_warehouse=warehouse)
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gt=start_date,
            equipment_delivery_tubemaster__gt=end_date,
            equipment_prep__lt=end_date,
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        PART = set()
        for i in project_qs:
            for j in i.part.all():
                PART.add(j.id)

        return Part.objects.exclude(id__in=PART).order_by("location_for_warehouse__id")


################################################################################
#            SupplyOrifice API View
################################################################################


class SupplyOrificeNewView(EquipAndPartGeneralView):
    queryset = Supply_orifice.objects.all()
    serializer_class = SupplyOrificeSerializer
    search_fields = [
        "serial_number",
        "storage_case",
    ]

    model_relation_name = "supply_orifice_part"


class SupplyOrificeView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Supply_orifice.objects.all()
    serializer_class = SupplyOrificeSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid")
        # Q()
        warehouse = self.request.query_params.get("warehouse")

        if warehouse:
            qs = qs.filter(location_for_warehouse=warehouse)
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gt=start_date,
            equipment_delivery_tubemaster__gt=end_date,
            equipment_prep__lt=end_date,
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        supply_orifice_part = set()

        for i in project_qs:
            for j in i.supply_orifice_part.all():
                supply_orifice_part.add(j.id)

        return qs.exclude(id__in=supply_orifice_part).order_by(
            "location_for_warehouse__id"
        )


################################################################################
#            Pressure API View
################################################################################


class PressureSensorNewView(EquipAndPartGeneralView):
    queryset = Pressure_sensor.objects.all()
    serializer_class = PressureSensorSerializer
    search_fields = [
        "serial_number",
        "part_name",
        "name_of_abbreviation",
        "asset_number",
        "packaging",
    ]

    model_relation_name = "pressure_sensor_part"


class PressureSensorView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Pressure_sensor.objects.all()
    serializer_class = PressureSensorSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid")
        # Q()
        warehouse = self.request.query_params.get("warehouse")

        if warehouse:
            qs = qs.filter(location_for_warehouse=warehouse)
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gt=start_date,
            equipment_delivery_tubemaster__gt=end_date,
            equipment_prep__lt=end_date,
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        pressure_sensor_part = set()
        for i in project_qs:
            for j in i.pressure_sensor_part.all():
                pressure_sensor_part.add(j.id)

        return Pressure_sensor.objects.exclude(id__in=pressure_sensor_part).order_by(
            "location_for_warehouse__id"
        )


################################################################################
#            calibration orifice API View
################################################################################


class CalibrationOrificeNewView(EquipAndPartGeneralView):
    queryset = Calibration_orifice.objects.all()
    serializer_class = CalibrationOrificeSerializer
    search_fields = [
        "serial_number",
        "part_name",
        "name_of_abbreviation",
        "asset_number",
    ]

    model_relation_name = "calibration_orifice_part"


class CalibrationOrificeView(ListAPIView):
    queryset = Calibration_orifice.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = CalibrationOrificeSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid")
        # Q()
        warehouse = self.request.query_params.get("warehouse")

        if warehouse:
            qs = qs.filter(location_for_warehouse=warehouse)
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gt=start_date,
            equipment_delivery_tubemaster__gt=end_date,
            equipment_prep__lt=end_date,
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        calibration_orifice_part = set()
        for i in project_qs:
            for j in i.calibration_orifice_part.all():
                calibration_orifice_part.add(j.id)

        return Calibration_orifice.objects.exclude(
            id__in=calibration_orifice_part
        ).order_by("location_for_warehouse__id")


################################################################################
#            swabmaster API View
################################################################################


class SwabMasterNewView(EquipAndPartGeneralView):
    queryset = SwabMasterTSR.objects.all()
    serializer_class = SwabMasterSerializer
    search_fields = [
        "serial_number",
        "tube_seal_rack",
        "part_name",
        "name_of_abbreviation",
        "asset_number",
    ]

    model_relation_name = "swabmaster_part"


class SwabMasterView(ListAPIView):
    queryset = SwabMasterTSR.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = SwabMasterSerializer

    def get_queryset(self):
        super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid")
        # Q()
        self.request.query_params.get("warehouse")

        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gt=start_date,
            equipment_delivery_tubemaster__gt=end_date,
            equipment_prep__lt=end_date,
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        swabmaster_part = set()

        for i in project_qs:
            for i in i.swabmaster_part.all():
                swabmaster_part.add(i.id)

        return SwabMasterTSR.objects.exclude(id__in=swabmaster_part).order_by(
            "location_for_warehouse__id"
        )


################################################################################
#            Devicehose API View
################################################################################


class DeviceHoseNewView(EquipAndPartGeneralView):
    queryset = DeviceHose.objects.all()
    serializer_class = DeviceHoseSerializer
    filter_backends = [SearchFilter]
    pagination_class = CustomPagination
    model_relation_name = "device_part"
    model_warehouse_field = "warehouse"

    search_fields = [
        "serial_number",
        "part_name",
        "name_of_abbreviation",
        "asset_number",
    ]


class DeviceHoseView(ListAPIView):
    queryset = DeviceHose.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = DeviceHoseSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid", None)
        # Q()
        warehouse = self.request.query_params.get("warehouse")

        if warehouse:
            qs = qs.filter(warehouse=warehouse)
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gt=start_date,
            equipment_delivery_tubemaster__gt=end_date,
            equipment_prep__lt=end_date,
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        device_part = set()
        for i in project_qs:
            for j in i.device_part.all():
                device_part.add(j.id)

        return DeviceHose.objects.exclude(id__in=device_part).order_by("warehouse__id")


################################################################################
#            Airhose API View
################################################################################


class AirHoseNewView(EquipAndPartGeneralView):
    queryset = AirHose.objects.all()
    serializer_class = AirHoseSerializer

    search_fields = [
        "serial_number",
        "colour_code",
        "part_name",
        "name_of_abbreviation",
        "asset_number",
    ]
    model_relation_name = "airhose_part"
    model_warehouse_field = "warehouse"


class AirHoseView(ListAPIView):
    queryset = AirHose.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = AirHoseSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = convert_to_date(self.request.query_params.get("start_date"))
        end_date = convert_to_date(self.request.query_params.get("end_date"))
        pro_id = self.request.query_params.get("proid")
        # Q()
        warehouse = self.request.query_params.get("warehouse")

        if warehouse:
            qs = qs.filter(warehouse=warehouse)
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        if start_date and end_date:
            project_qs = Project.objects.filter(
                equipment_prep__gte=start_date,
                equipment_delivery_tubemaster__lte=end_date,
            )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        airhose_part = set()
        for i in project_qs:
            for j in i.airhose_part.all():
                airhose_part.add(j.id)

        return qs.exclude(id__in=airhose_part).order_by("warehouse__id")


################################################################################
#                           All List View API Project
################################################################################


class ProjectAllListView(generics.ListAPIView):
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        "created_at",
    ]

    search_fields = [
        "project_name",
        "project_number",
        "project_start",
        "project_end",
        "client__official_name",
        "equipment_delivery_tubemaster",
        "unit__name_of_unit",
    ]
    ordering = ["created_at"]
    queryset = Project.objects.all()
    serializer_class = Add_Project_serializer
    pagination_class = CustomPagination

    filterset_fields = ["client", "project_start", "project_end"]


################################################################################
#                        All Create View API Project
################################################################################


class ProjectAllCreateView(generics.CreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Project.objects.all()
    serializer_class = Create_Project_Serializer


################################################################################
#                           ListAll View API Project
################################################################################


class AallList_Id_Project(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = Add_Project_serializer
    queryset = Project.objects.all()

    lookup_field = "slug"


################################################################################
#                           get 1 project with no depth View API Project
################################################################################


class getlList_Id_Project(generics.RetrieveAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = GET_Project_serializer
    queryset = Project.objects.all()

    lookup_field = "slug"


class updateProject(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreateProjectSerializer
    queryset = Project.objects.all()

    lookup_field = "slug"


################################################################################
#                           UpdateAll View API Project
################################################################################


class AllList_Id_Patch_Project(generics.RetrieveUpdateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = Create_Project_Serializer
    queryset = Project.objects.all()

    lookup_field = "slug"


from django_auto_prefetching import AutoPrefetchViewSetMixin
from silk.profiling.profiler import silk_profile


class ProjectRecordView(AutoPrefetchViewSetMixin, generics.RetrieveAPIView):
    queryset = Project.objects.all()

    serializer_class = ProjectRecordSerializer
    lookup_field = "slug"

    @silk_profile(name="reports")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
