from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .serializers import *
from tm_api.paginator import CustomPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import api_view
from datetime import datetime
import pytz
from project.models import Project

################################################################################
#                UpddateAll View API Project/ SupplyOrificeViewPart
################################################################################


# class SupplyOrificeViewPart(generics.ListAPIView):
#     permission_classes = [DjangoModelPermissions, IsAdminUser]
#     authentication_classes= [ JWTAuthentication]

#     serializer_class = SupplyOrificeSerializer
#     queryset = Supply_orifice.objects.all()

#     ttd = TTD_tube_seal_rack.objects.all()
#     for a in ttd:
#         ttd.exclude(id = queryset)
#         retu
from equipment.models import *


class SupplyOrificeViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    serializer_class = SupplyOrificeSerializer
    queryset = Supply_orifice.objects.all()
    # def get_queryset(self):
    #     so = set()
    #     for ttd in TTD.objects.all():
    #         so.add(ttd.supply_orifice_set.id)
    #     so_qs = Supply_orifice.objects.exclude(id__in = so)
    #     return so_qs

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
    # def get_queryset(self):
    #     so = set()
    #     for ttd in TTD.objects.all():
    #         so.add(ttd.pressure_sensor.id)
    #     so_qs = Pressure_sensor.objects.exclude(id__in = so)
    #     return so_qs

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

    # def get_queryset(self):
    #     so = set()
    #     for ttd in TTD.objects.all():
    #         so.add(ttd.TTD_tube_seal_rack.id)
    #     so_qs = TTD_tube_seal_rack.objects.exclude(id__in = so)
    #     return so_qs

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

from rest_framework.parsers import MultiPartParser, FormParser


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
        # current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()
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
            qs = qs.filter(location_for_warehouse=warehouse)
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
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        queryset = BDD_tube_seal_rack.objects.all()

        if warehouse:
            queryset = queryset.filter(location_for_warehouse=warehouse)
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
            qs = qs.filter(location_for_warehouse=warehouse)

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
            qs = qs.filter(location_for_warehouse=warehouse)

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
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        queryset = Part.objects.all()
        free = self.request.GET.get("free")
        if free:
            used_id = set()
            for i in Project.objects.all():
                if i.equipment_delivery_client > current_datetime:
                    if i.part:
                        for j in i.part.all():
                            used_id.add(j.id)

            queryset = queryset.exclude(id__in=used_id)

        if warehouse:
            queryset = queryset.filter(location_for_warehouse__slug=warehouse)
        return queryset


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


class AllGeneralPartRetUpdDelView(generics.RetrieveUpdateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = AllGeneralPartCreateSerializer
    queryset = Part.objects.all()

    lookup_field = "slug"


@api_view(["GET"])
def warehouse_part_view(request):
    pagination_class = CustomPagination()
    print(request.query_params.get("pm_status"))

    serializer = WarehousePartSerializer(context={"request": request})
    part_data = serializer.get_general_part(None)
    supply_orifice_data = serializer.get_supply_orifice(None)
    pressure_sensor_data = serializer.get_pressure_sensor(None)
    ttd_rack_data = serializer.get_ttd_rack(None)
    bdd_rack_data = serializer.get_bdd_rack(None)
    calibration_orifice_data = serializer.get_calibration_orifice(None)
    swabmaster_data = serializer.get_swabmasterTSR(None)
    devicehose_data = serializer.get_devicehose(None)
    airhose_data = serializer.get_airhose(None)

    merged_data = (
        part_data
        + supply_orifice_data
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
        "part_data": len(part_data),
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
