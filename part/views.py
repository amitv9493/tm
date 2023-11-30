from datetime import datetime

import pytz
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from equipment.models import *
from project.models import Project
from tm_api.paginator import CustomPagination

from .models import *
from .serializers import *


class SupplyOrificeViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = SupplyOrificeSerializer
    queryset = Supply_orifice.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["location_for_warehouse"]

    def get_queryset(self):
        qs = super().get_queryset()
        ttd_id = self.request.GET.get("ttd_id")
        warehouse = self.request.GET.get("warehouse")
        so = set()

        if ttd_id:
            for ttd in TTD.objects.exclude(slug=ttd_id):
                if ttd.supply_orifice_set:
                    so.add(ttd.supply_orifice_set.id)

        else:
            for ttd in TTD.objects.all():
                if ttd.supply_orifice_set:
                    so.add(ttd.supply_orifice_set.id)

        return (
            qs.exclude(id__in=so)
            if not warehouse
            else qs.exclude(id__in=so).filter(location_for_warehouse__slug=warehouse)
        )


##################################################################################
#                  PressureSensor View
##################################################################################


class PressureSensorViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Pressure_sensor.objects.all()
    serializer_class = PressureSensorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["location_for_warehouse"]

    def get_queryset(self):
        qs = super().get_queryset()
        ttd_id = self.request.GET.get("ttd_id")
        warehouse_id = self.request.GET.get("warehouse_id")

        pressure_sensor = set()
        if ttd_id:
            for ttd in TTD.objects.exclude(slug=ttd_id):
                if ttd.pressure_sensor:
                    pressure_sensor.add(ttd.pressure_sensor.id)

        else:
            for ttd in TTD.objects.all():
                if ttd.pressure_sensor:
                    pressure_sensor.add(ttd.pressure_sensor.id)

        return (
            qs.exclude(id__in=pressure_sensor)
            if not warehouse_id
            else qs.exclude(id__in=pressure_sensor).filter(
                location_for_warehouse__slug=warehouse_id
            )
        )


##################################################################################
#                  TTDTubeSealRack  View
##################################################################################


class TTDTubeSealRackViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = TTD_tube_seal_rack.objects.all()
    serializer_class = TTDTubeSealRackSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        ttd_id = self.request.GET.get("ttd_id")
        warehouse_id = self.request.GET.get("warehouse_id")

        so = set()  # Initialize the 'so' variable here
        if ttd_id:
            for ttd in TTD.objects.exclude(slug=ttd_id):
                if ttd.TTD_tube_seal_rack:
                    so.add(ttd.TTD_tube_seal_rack.id)
        else:
            for ttd in TTD.objects.all():
                if ttd.TTD_tube_seal_rack:
                    so.add(ttd.TTD_tube_seal_rack.id)

        return (
            qs.exclude(id__in=so)
            if not warehouse_id
            else qs.exclude(id__in=so).filter(location_for_warehouse__slug=warehouse_id)
        )


##################################################################################
#                  BDDTubeSealRack  View
##################################################################################


class BDDTubeSealRackViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = BDDTubeSealRackSerializer
    queryset = BDD_tube_seal_rack.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["location_for_warehouse"]

    def get_queryset(self):
        qs = super().get_queryset()
        bdd_id = self.request.GET.get("bdd_id")
        warehouse_id = self.request.GET.get("warehouse_id")

        so = set()

        if bdd_id:
            for bdd in BDD.objects.exclude(slug=bdd_id):
                if bdd.BDD_tube_seal_rack:
                    so.add(bdd.BDD_tube_seal_rack.id)
        else:
            for bdd in BDD.objects.all():
                if bdd.BDD_tube_seal_rack:
                    so.add(bdd.BDD_tube_seal_rack.id)

        return (
            qs.exclude(id__in=so)
            if not warehouse_id
            else qs.exclude(id__in=so).filter(location_for_warehouse__slug=warehouse_id)
        )


################################################################################
#                SwabMaster View
################################################################################


class SwabMasterTSRViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = SwabMasterTSR.objects.all()
    serializer_class = SwabMasterTSRSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["location_for_warehouse"]

    def get_queryset(self):
        qs = super().get_queryset()
        swab_id = self.request.GET.get("swab_id")
        warehouse_id = self.request.GET.get("warehouse_id")

        swabmaster_id = set()
        if swab_id:
            for swab in SwabMaster.objects.exclude(slug=swab_id):
                if swab.Swab_Master_Tube_Seal_Rack:
                    swabmaster_id.add(swab.Swab_Master_Tube_Seal_Rack.id)

        return (
            qs.exclude(id__in=swabmaster_id)
            if not warehouse_id
            else qs.exclude(id__in=swabmaster_id).filter(
                location_for_warehouse__slug=warehouse_id
            )
        )


################################################################################
#                DeviceHose View
################################################################################


class DeviceHoseRViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = DeviceHoseSerializer
    queryset = DeviceHose.objects.all()


################################################################################
#                AirHose View
################################################################################


class AirHoseViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    serializer_class = AirHoseSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "pm_status",
    ]
    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
        "price",
    ]

    def get_queryset(self):
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        queryset = AirHose.objects.all()
        free = self.request.GET.get("free")
        if free:
            used_id = set()
            for i in Project.objects.all():
                if i.equipment_delivery_client > current_datetime:
                    if i.airhose_part:
                        for j in i.airhose_part.all():
                            used_id.add(j.id)

            queryset = queryset.exclude(id__in=used_id)

        if warehouse:
            queryset = queryset.filter(warehouse__slug=warehouse)
        return queryset


#######################################################################
#                     CalibrationOrificeViewPart for options
#######################################################################


class CalibrationOrificeViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = Calibration_orifice_serializer
    queryset = Calibration_orifice.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["location_for_warehouse"]

    def get_queryset(self):
        qs = super().get_queryset()
        cr_id = self.request.GET.get("cr_id")
        warehouse_id = self.request.GET.get("warehouse_id")

        so = set()

        if cr_id:
            for cr in CALIBRATION_STAND.objects.exclude(slug=cr_id):
                if cr.calibration_orifice_set:
                    so.add(cr.calibration_orifice_set.id)

        else:
            for cr in CALIBRATION_STAND.objects.all():
                if cr.calibration_orifice_set:
                    so.add(cr.calibration_orifice_set.id)

        return (
            qs.exclude(id__in=so)
            if not warehouse_id
            else qs.exclude(id__in=so).filter(location_for_warehouse__slug=warehouse_id)
        )


#######################################################################
#                     AirHose-CreateView
#######################################################################


class AirHoseCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = AirHoseCreSerializer
    queryset = AirHose.objects.all()


#######################################################################
#                     AirHose-RetUpdDelView
#######################################################################

from rest_framework.parsers import FormParser, MultiPartParser


class AirHoseRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = AirHoseCreSerializer
    queryset = AirHose.objects.all()

    lookup_field = "slug"


#######################################################################
#                     DeviceHose-ListView
#######################################################################


class DeviceHoseRListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    serializer_class = DeviceHoseListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["pm_status"]
    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
        "price",
    ]

    def get_queryset(self):
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        queryset = DeviceHose.objects.all()
        free = self.request.GET.get("free")
        if free:
            used_id = set()
            for i in Project.objects.all():
                if i.equipment_delivery_client > current_datetime:
                    if i.device_part:
                        for j in i.device_part.all():
                            used_id.add(j.id)

            queryset = queryset.exclude(id__in=used_id)

        if warehouse:
            queryset = queryset.filter(warehouse__slug=warehouse)
        return queryset


#######################################################################
#                     DeviceHose-CreateView
#######################################################################


class DeviceHoseRCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = DeviceHoseCreateSerializer
    queryset = DeviceHose.objects.all()


#######################################################################
#                     DeviceHose-RetUpdDelView
#######################################################################


class DeviceHoseRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = DeviceHoseCreateSerializer
    queryset = DeviceHose.objects.all()

    lookup_field = "slug"


#######################################################################
#                     SwabMaster-ListView
#######################################################################


class SwabMasterTSRListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = SwabMasterTSR.objects.all()

    pagination_class = CustomPagination
    serializer_class = SwabMasterTSRSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "pm_status",
    ]
    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
        "price",
    ]

    def get_queryset(self):
        qs = super().get_queryset()
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        free = self.request.GET.get("free")
        if free:
            # used_id = set()
            # for i in Project.objects.all():
            #     if i.equipment_delivery_client > current_datetime:
            #         if i.swabmaster_part:
            #             for j in i.swabmaster_part.all():
            #                 used_id.add(j.id)

            # queryset = queryset.exclude(id__in=used_id)
            qs = qs.filter(swabmaster__isnull=True)

        if warehouse:
            qs = qs.filter(location_for_warehouse__slug=warehouse)
        return qs


#######################################################################
#                     SwabMaster-CreateView
#######################################################################


class SwabMasterTSRCreateView(generics.ListCreateAPIView):
    ermission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = SwabMasterTSRCreateSerializer
    queryset = SwabMasterTSR.objects.all()


#######################################################################
#                     SwabMaster-RetUpdDelView
#######################################################################


class SwabMasterTSRRetUpdDelViewl(generics.RetrieveUpdateAPIView):
    ermission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = SwabMasterTSRCreateSerializer
    queryset = SwabMasterTSR.objects.all()

    lookup_field = "slug"


#######################################################################
#                     CalibrationOrifice-ListView
#######################################################################


class CalibrationOrificeListView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    serializer_class = CalibratiobOrificeSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "pm_status",
    ]
    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
        "price",
    ]

    def get_queryset(self):
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        queryset = Calibration_orifice.objects.all()
        free = self.request.GET.get("free")
        if free:
            used_id = set()
            for i in Project.objects.all():
                if i.equipment_delivery_client > current_datetime:
                    if i.calibration_orifice_part:
                        for j in i.calibration_orifice_part.all():
                            used_id.add(j.id)

            queryset = queryset.exclude(id__in=used_id)

        if warehouse:
            queryset = queryset.filter(location_for_warehouse__slug=warehouse)
        return queryset


#######################################################################
#                     CalibrationOrifice-CreateView
#######################################################################


class CalibrationOrificeCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = CalibratiobOrificeCreateSerializer
    queryset = Calibration_orifice.objects.all()


#######################################################################
#                     CalibrationOrifice-RetUpdDelView
#######################################################################


class CalibrationOrificeRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = CalibratiobOrificeCreateSerializer
    queryset = Calibration_orifice.objects.all()

    lookup_field = "slug"


#######################################################################
#                     BddTubesealrack-ListViewView
#######################################################################


class BddTubesealrackList(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    serializer_class = BddTubesealrackListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "pm_status",
    ]
    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
        "price",
    ]

    def get_queryset(self):
        warehouse = self.request.query_params.get("warehouse")
        queryset = BDD_tube_seal_rack.objects.all()

        if warehouse:
            queryset = queryset.filter(location_for_warehouse__slug=warehouse)
        return queryset


#######################################################################
#                     BddTubesealrack-CreateView
#######################################################################


class BddTubesealrackCreate(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = BddTubesealrackCreateSerializer
    queryset = BDD_tube_seal_rack.objects.all()


#######################################################################
#                     BddTubesealrack-RetUpdDelView
#######################################################################


class BddTubesealrackRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = BddTubesealrackCreateSerializer
    queryset = BDD_tube_seal_rack.objects.all()

    lookup_field = "slug"


#######################################################################
#                     TddTubesealrack-ListViewView
#######################################################################


class TddTubesealrackList(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    serializer_class = TddTubesealrackListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "pm_status",
    ]
    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
        "price",
    ]

    def get_queryset(self):
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        queryset = TTD_tube_seal_rack.objects.all()

        if warehouse:
            queryset = queryset.filter(location_for_warehouse__slug=warehouse)
        return queryset


#######################################################################
#                     TddTubesealrack-CreateView
#######################################################################


class TddTubesealrackCreate(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = TddTubesealrackCreateSerializer
    queryset = TTD_tube_seal_rack.objects.all()


#######################################################################
#                     TddTubesealrack-RetUpdDelView
#######################################################################


class TddTubesealrackRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = TddTubesealrackCreateSerializer
    queryset = TTD_tube_seal_rack.objects.all()

    lookup_field = "slug"


#######################################################################
#                     PressureSensor-ListView
#######################################################################


class PressureSensorListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    queryset = Pressure_sensor.objects.all()

    serializer_class = PressuresensorListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "pm_status",
    ]
    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
        "price",
    ]

    def get_queryset(self):
        qs = super().get_queryset()

        warehouse = self.request.query_params.get("warehouse")
        free = self.request.GET.get("free")
        if free:
            # used_id = set()
            # for i in Project.objects.all():
            #     if i.equipment_delivery_client > current_datetime:
            #         if i.pressure_sensor_part:
            #             for j in i.pressure_sensor_part.all():
            #                 used_id.add(j.id)

            # queryset = queryset.exclude(id__in=used_id)
            qs = qs.filter(TTD__isnull=True)

        if warehouse:
            qs = qs.filter(location_for_warehouse__slug=warehouse)

        return qs


#######################################################################
#                     PressureSensor-CreateView
#######################################################################


class PressureSensorCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = PressuresensorCreateSerializer
    queryset = Pressure_sensor.objects.all()


#######################################################################
#                     PressureSensor-RetUpdDelView
#######################################################################


class PressureSensorRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = PressuresensorCreateSerializer
    queryset = Pressure_sensor.objects.all()

    lookup_field = "slug"


#######################################################################
#                     SupplyOrificeListView-ListView
#######################################################################


class SupplyOrificeListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    queryset = Supply_orifice.objects.all()

    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    serializer_class = SupplyOrificeListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "pm_status",
    ]
    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
        "price",
    ]

    def get_queryset(self):
        qs = super().get_queryset()
        # current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()
        warehouse = self.request.query_params.get("warehouse")
        free = self.request.GET.get("free")
        if free:
            # used_id = set()
            # for i in Project.objects.all():
            #     if i.equipment_delivery_client > current_datetime:
            #         if i.supply_orifice_part:
            #             for j in i.supply_orifice_part.all():
            #                 used_id.add(j.id)

            # queryset = queryset.exclude(id__in=used_id)
            qs.filter(TTD__isnull=True)

        if warehouse:
            qs = qs.filter(location_for_warehouse__slug=warehouse)

        return qs


#######################################################################
#                     SupplyOrificeListView-ListView
#######################################################################


class SupplyOrificeCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = SupplyOrificeCreateSerializer
    queryset = Supply_orifice.objects.all()


#######################################################################
#                     SupplyOrificeListView-RetUpdDelView
#######################################################################


class SupplyOrificeRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = SupplyOrificeCreateSerializer
    queryset = Supply_orifice.objects.all()

    lookup_field = "slug"


#######################################################################
#                     AllgeneralPart-ListView
#######################################################################


class AllGeneralPartListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    queryset = Part.objects.select_related("location_for_warehouse")

    serializer_class = AllGeneralPartListSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "pm_status",
    ]
    search_fields = [
        "part_name",
        "name_of_abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
        "price",
    ]

    def get_queryset(self):
        qs = super().get_queryset()
        datetime.now(pytz.timezone("Asia/Kolkata")).date()
        start_date = self.request.query_params.get("date")
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        free = self.request.GET.get("free")
        if free:
            project_qs = Project.objects.filter(
                equipment_delivery_tubemaster__gt=start_date,
            )

            used_id = set(project_qs.values_list("part", flat=True))

            qs = qs.exclude(id__in=used_id)

        if warehouse:
            qs = qs.filter(location_for_warehouse__slug=warehouse)

        if start_date:
            project_qs = Project.objects.filter(
                equipment_delivery_tubemaster__gte=start_date,
            )

            exclude_objects = set(project_qs.values_list("part", flat=True))

            qs = qs.exclude(id__in=exclude_objects)

        return qs


#######################################################################
#                     AllgeneralPart-CreateView
#######################################################################


class AllGeneralPartCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = AllGeneralPartCreateSerializer
    queryset = Part.objects.all()


#######################################################################
#                     AllgeneralPart-RetUpdDelView
#######################################################################

from core.utils import get_exclude_objects


class AllGeneralPartRetUpdDelView(generics.RetrieveUpdateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = AllGeneralPartCreateSerializer
    queryset = Part.objects.all()

    lookup_field = "slug"


@api_view(["GET"])
def warehouse_part_view(request):
    pagination_class = CustomPagination()

    slug = request.query_params.get("slug")
    pm_status = str(request.query_params.get("pm_status")).upper()
    start_date = request.query_params.get("start_date")

    common_query = Q()
    exception_query = Q()
    if pm_status != "NONE":
        common_query &= Q(pm_status=pm_status)
        exception_query &= Q(pm_status=pm_status)

    if slug:
        exception_query &= Q(warehouse__slug=slug)
        common_query &= Q(location_for_warehouse__slug=slug)

    supply_orifice_data = SupplyOrificeCreateSerializer(
        Supply_orifice.objects.filter(common_query),
        many=True,
    ).data

    pressure_sensor_data = PressureSensorSerializer(
        Pressure_sensor.objects.filter(common_query),
        many=True,
    ).data
    ttd_rack_data = TddTubesealrackCreateSerializer(
        TTD_tube_seal_rack.objects.filter(common_query), many=True
    ).data
    bdd_rack_data = BDDTubeSealRackSerializer(
        BDD_tube_seal_rack.objects.filter(common_query), many=True
    ).data

    swabmaster_data = SwabMasterTSRSerializer(
        SwabMasterTSR.objects.filter(common_query), many=True
    ).data

    # =============================================

    devicehose_data = DeviceHoseSerializer(
        DeviceHose.objects.filter(exception_query).exclude(
            id__in=get_exclude_objects(start_date, "device_part")
        ),
        many=True,
    ).data
    airhose_data = AirHoseSerializer(
        AirHose.objects.filter(exception_query).exclude(
            id__in=get_exclude_objects(start_date, "airhose_part")
        ),
        many=True,
    ).data
    calibration_orifice_data = Calibration_orifice_serializer(
        Calibration_orifice.objects.filter(common_query).exclude(
            id__in=get_exclude_objects(start_date, "calibration_orifice_part")
        ),
        many=True,
    ).data

    merged_data = (
        supply_orifice_data
        + pressure_sensor_data
        + ttd_rack_data
        + bdd_rack_data
        + calibration_orifice_data
        + swabmaster_data
        + devicehose_data
        + airhose_data
    )

    paginated_data = pagination_class.paginate_queryset(merged_data, request)

    paginated_data_with_counts = {
        "supply_orifice_data": len(supply_orifice_data),
        "pressure_sensor_data": len(pressure_sensor_data),
        "ttd_rack_data": len(ttd_rack_data),
        "bdd_rack_data": len(bdd_rack_data),
        "calibration_orifice_data": len(calibration_orifice_data),
        "swabmaster_data": len(swabmaster_data),
        "devicehose_data": len(devicehose_data),
        "airhose_data": len(airhose_data),
        "results": paginated_data,
    }
    return pagination_class.get_paginated_response(paginated_data_with_counts)


class AllGeneralPart(generics.ListAPIView):
    queryset = Part.objects.all()
    serializer_class = AllGeneralPartCreateSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = super().get_queryset()

        slug = self.request.query_params.get("slug")
        pm_status = str(self.request.query_params.get("pm_status")).upper()

        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)

        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)

        return qs
