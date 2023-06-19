from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from .serializers import LoginSerializer
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import ValidationError
from rest_framework import filters


# from .persmissions import Mypermission
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .serializers import *

# from application.models import Application
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

# from django_filters.rest_framework import DjangoFilterBackend
# from .renderers import UserRenderes
# from .paginator import CustomPagination
# from enquiry.models import Course

from rest_framework.response import Response
from rest_framework.views import APIView
from .paginator import CustomPagination
from project.models import *
from part.models import *
from equipment.models import *

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
                    print("No group assigned to user")
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
#            Client API View
###################################################################################
from .paginator import CustomPagination


class ClientListView(ListAPIView):
    # pagination_class = CustomPagination
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes= [ JWTAuthentication]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


###################################################################################
#            Unit API View
###################################################################################


class UnitListView(ListAPIView):
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        if start_date and end_date:
            qs = Project.objects.filter(
                equipment_prep__gte=start_date,
                equipment_delivery_tubemaster__lte=end_date,
            )
        if pro_id:
            qs = qs.exclude(id=pro_id)

        unit = set()
        for i in qs:
            for i in i.unit.all():
                unit.add(i.id)
        unit = list(unit)
        unit_qs = Unit.objects.exclude(id__in=unit)
        return unit_qs


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
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes = [ JWTAuthentication ]
    # queryset = Unit.objects.all()
    serializer_class = ReactorSerializer

    def get_queryset(self):
        # qs =  super().get_queryset()
        client_id = self.request.query_params.get("client")
        unit_id = self.request.query_params.get("unit")
        print(client_id)
        print(unit_id)
        queryset = Reactor.objects.filter(client=client_id, unit=unit_id)
        return queryset


################################################################################
#                    TTD API View
################################################################################


# from django.db import Q

# class TtdView(ListAPIView):
#     permission_classes = [DjangoModelPermissions, IsAdminUser]
#     authentication_classes= [ JWTAuthentication]
#     queryset  = TTD.objects.all()
#     serializer_class = TtdSerializer


#     def get_queryset(self):
#         qs =  super().get_queryset()

#         start_date = self.request.query_params.get('start_date')
#         end_date = self.request.query_params.get('end_date')
#         print(start_date)
#         print(end_date)
#         # Q()
#         qs = Project.objects.filter(equipment_prep__gte = start_date ,equipment_delivery_tubemaster__lte = end_date)

#         # print(qs.ttd)
#         ttd  = set()
#         for i in qs:
#             for i in i.ttd.all():
#                 ttd.add(i.id)


#         ttd = list(ttd)
#         ttd_qs = TTD.objects.exclude(id__in = ttd)
#         return (ttd_qs)
class SwabMasterEquipmentView(ListAPIView):
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = [
        "serial_number",
        "pm_status",
        "alternate_name",
    ]
    queryset = SwabMaster.objects.all()
    serializer_class = SwabMasterSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            # return
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)

        swabmaster = set()
        for i in project_qs:
            for j in i.swabmaster_equip.all():
                swabmaster.add(j.id)
        # ttd = list(ttd)

        return qs.exclude(id__in=swabmaster)


class TTDNewView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = [
        "serial_number",
        "pm_status",
        "alternate_name",
    ]
    queryset = TTD.objects.all()
    serializer_class = TtdSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)

        ttd = set()
        for i in project_qs:
            for j in i.ttd.all():
                ttd.add(j.id)
        # ttd = list(ttd)

        return qs.exclude(id__in=ttd)


class TtdView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    # pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = [
        "serial_number",
        "pm_status",
        "alternate_name",
    ]
    queryset = TTD.objects.all()
    serializer_class = TtdSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        print(start_date)
        print(end_date)

        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")
        # Q()
        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)

        ttd = set()
        for i in project_qs:
            for j in i.ttd.all():
                ttd.add(j.id)

        return qs.exclude(id__in=ttd)


################################################################################
#            BDD API View
################################################################################


class BddNewView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = BDD.objects.all()
    serializer_class = BddSerializer
    pagination_class = CustomPagination

    filter_backends = [SearchFilter]
    search_fields = [
        "serial_number",
        "pm_status",
        "alternate_name",
    ]

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        print(start_date)
        print(end_date)
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        bdd = set()
        for i in project_qs:
            for j in i.bdd.all():
                bdd.add(j.id)

        return qs.exclude(id__in=bdd)


class BddView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = BDD.objects.all()
    serializer_class = BddSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        print(start_date)
        print(end_date)
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        bdd = set()
        for i in project_qs:
            for j in i.bdd.all():
                bdd.add(j.id)

        return qs.exclude(id__in=bdd)


################################################################################
#            Calibration API View
################################################################################


class CalibrationStandNewView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = CALIBRATION_STAND.objects.all()
    serializer_class = CALIBRATION_STANDSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = [
        "serial_number",
        "pm_status",
        "alternate_name",
    ]

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        print(start_date)
        print(end_date)
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        calibration_stand = set()
        for i in project_qs:
            for j in i.calibration_stand.all():
                calibration_stand.add(j.id)

        return qs.exclude(id__in=calibration_stand)


class CalibrationStandView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = CALIBRATION_STAND.objects.all()
    serializer_class = CALIBRATION_STANDSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        print(start_date)
        print(end_date)
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        calibration_stand = set()
        for i in project_qs:
            for j in i.calibration_stand.all():
                calibration_stand.add(j.id)

        return qs.exclude(id__in=calibration_stand)


################################################################################
#                        Part API View
################################################################################


class PartNewView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    pagination_class = CustomPagination

    filter_backends = [SearchFilter]
    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
    ]

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        PART = set()
        for i in project_qs:
            for j in i.part.all():
                PART.add(j.id)

        return Part.objects.exclude(id__in=PART)


class PartView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Part.objects.all()
    serializer_class = PartSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        PART = set()
        for i in project_qs:
            for j in i.part.all():
                PART.add(j.id)

        return Part.objects.exclude(id__in=PART)


################################################################################
#            SupplyOrifice API View
################################################################################


class SupplyOrificeNewView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Supply_orifice.objects.all()
    serializer_class = SupplyOrificeSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = [
        "serial_number",
        "storage_case",
    ]

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        supply_orifice_part = set()

        for i in project_qs:
            for j in i.supply_orifice_part.all():
                supply_orifice_part.add(j.id)

        return qs.exclude(id__in=supply_orifice_part)


class SupplyOrificeView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Supply_orifice.objects.all()
    serializer_class = SupplyOrificeSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        supply_orifice_part = set()

        for i in project_qs:
            for j in i.supply_orifice_part.all():
                supply_orifice_part.add(j.id)

        return qs.exclude(id__in=supply_orifice_part)


################################################################################
#            Pressure API View
################################################################################


class PressureSensorNewView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Pressure_sensor.objects.all()
    serializer_class = PressureSensorSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = [
        "serial_number",
        "part_name",
        "name_of_abbreviation",
        "asset_number",
        "packaging",
    ]

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        pressure_sensor_part = set()
        for i in project_qs:
            for j in i.pressure_sensor_part.all():
                pressure_sensor_part.add(j.id)

        return Pressure_sensor.objects.exclude(id__in=pressure_sensor_part)


class PressureSensorView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Pressure_sensor.objects.all()
    serializer_class = PressureSensorSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        pressure_sensor_part = set()
        for i in project_qs:
            for j in i.pressure_sensor_part.all():
                pressure_sensor_part.add(j.id)

        return Pressure_sensor.objects.exclude(id__in=pressure_sensor_part)


################################################################################
#            calibrtion orofic API View
################################################################################


class CalibrationOrificeNewView(ListAPIView):
    queryset = Calibration_orifice.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = CalibrationOrificeSerializer
    filter_backends = [SearchFilter]
    pagination_class = CustomPagination
    search_fields = [
        "serial_number",
        "part_name",
        "name_of_abbreviation",
        "asset_number",
    ]

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        calibration_orifice_part = set()
        for i in project_qs:
            for j in i.calibration_orifice_part.all():
                calibration_orifice_part.add(j.id)

        return Calibration_orifice.objects.exclude(id__in=calibration_orifice_part)


class CalibrationOrificeView(ListAPIView):
    queryset = Calibration_orifice.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = CalibrationOrificeSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        calibration_orifice_part = set()
        for i in project_qs:
            for j in i.calibration_orifice_part.all():
                calibration_orifice_part.add(j.id)

        return Calibration_orifice.objects.exclude(id__in=calibration_orifice_part)


################################################################################
#            swabmaster API View
################################################################################


class SwabMasterNewView(ListAPIView):
    queryset = SwabMasterTSR.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = SwabMasterSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = [
        "serial_number",
        "tube_seal_rack",
        "part_name",
        "name_of_abbreviation",
        "asset_number",
    ]

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        swabmaster_part = set()

        for i in project_qs:
            for i in i.swabmaster_part.all():
                swabmaster_part.add(i.id)

        return SwabMasterTSR.objects.exclude(id__in=swabmaster_part)


class SwabMasterView(ListAPIView):
    queryset = SwabMasterTSR.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = SwabMasterSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        swabmaster_part = set()

        for i in project_qs:
            for i in i.swabmaster_part.all():
                swabmaster_part.add(i.id)

        return SwabMasterTSR.objects.exclude(id__in=swabmaster_part)


################################################################################
#            Devicehose API View
################################################################################


class DeviceHoseNewView(ListAPIView):
    queryset = DeviceHose.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = DeviceHoseSerializer
    filter_backends = [SearchFilter]
    pagination_class = CustomPagination
    search_fields = [
        "serial_number",
        "part_name",
        "name_of_abbreviation",
        "asset_number",
    ]

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        device_part = set()
        for i in project_qs:
            for j in i.device_part.all():
                device_part.add(j.id)

        return DeviceHose.objects.exclude(id__in=device_part)


class DeviceHoseView(ListAPIView):
    queryset = DeviceHose.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = DeviceHoseSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
        if not start_date or not end_date:
            raise ValidationError("Both start_date and end_date are required.")

        project_qs = Project.objects.filter(
            equipment_prep__gte=start_date, equipment_delivery_tubemaster__lte=end_date
        )
        if pro_id:
            project_qs = project_qs.exclude(id=pro_id)
        # print(qs.ttd)
        device_part = set()
        for i in project_qs:
            for j in i.device_part.all():
                device_part.add(j.id)

        return DeviceHose.objects.exclude(id__in=device_part)


################################################################################
#            Airhose API View
################################################################################


class AirHoseNewView(ListAPIView):
    queryset = AirHose.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = AirHoseSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = [
        "serial_number",
        "colour_code",
        "part_name",
        "name_of_abbreviation",
        "asset_number",
    ]

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
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

        return qs.exclude(id__in=airhose_part)


class AirHoseView(ListAPIView):
    queryset = AirHose.objects.all()
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = AirHoseSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        pro_id = self.request.query_params.get("proid")
        # Q()
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

        return qs.exclude(id__in=airhose_part)


################################################################################
#                           All List View API Project
################################################################################


class ProjectAllListView(generics.ListAPIView):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        "created_at",
    ]
    ordering = ["created_at"]
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes= [ JWTAuthentication]
    queryset = Project.objects.all()
    serializer_class = Add_Project_serializer
    pagination_class = CustomPagination

    def perform_create(self, add_project_serializer):
        pass
        # add_project_serializer.save(created_by=self.request.user)


################################################################################
#                        All Create View API Project
################################################################################


class ProjectAllCreateView(generics.CreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Project.objects.all()
    serializer_class = Create_Project_Serializer

    # def perform_create(self, Create_Project_Serializer):
    #     Create_Project_Serializer.save(created_by=self.request.user)
    #     return super().perform_create(Create_Project_Serializer)


################################################################################
#                           ListAll View API Project
################################################################################


class AallList_Id_Project(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = Add_Project_serializer
    queryset = Project.objects.all()


################################################################################
#                           get 1 project with no depth View API Project
################################################################################


class getlList_Id_Project(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes= [ JWTAuthentication]

    serializer_class = GET_Project_serializer
    queryset = Project.objects.all()


################################################################################
#                           UpddateAll View API Project
################################################################################


class AallList_Id_Patch_Project(generics.RetrieveUpdateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = All_Project_Patch_serializer
    queryset = Project.objects.all()
