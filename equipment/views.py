from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from tube.models import Warehouse
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from project.models import Project
from datetime import datetime
import pytz
from rest_framework.response import Response
from tm_api.paginator import CustomPagination
from rest_framework import status

##################################################################
#       TTD List-View
##################################################################
import random


class TaskView(ListAPIView):
    serializer_class = TaskSerializer
    queryset = TTD.objects.all()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        number = random.randint(1, 100)
        if number % 5 == 0:
            return Response(
                {"msg": "An 500 Error Occured"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        if number & 2 == 0:
            return Response(
                {"msg": "A 404 Error Occured"}, status=status.HTTP_404_NOT_FOUND
            )

        else:
            return response


class TTDListView(ListAPIView):
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    serializer_class = TTDSerializers
    pagination_class = CustomPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ["pm_status", "alternate_name"]
    search_fields = [
        "alternate_name",
        "abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
    ]

    def get_queryset(self):
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        queryset = TTD.objects.all()
        free = self.request.GET.get("free")
        if free:
            used_id = set()
            for i in Project.objects.all():
                if i.equipment_delivery_client > current_datetime:
                    if i.ttd:
                        for j in i.ttd.all():
                            used_id.add(j.id)

            queryset = queryset.exclude(id__in=used_id)

        if warehouse:
            queryset = queryset.filter(location_for_warehouse__slug=warehouse)
        return queryset



##################################################################
#       TTD Create-View
##################################################################


class TTDCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = TTD.objects.all()
    serializer_class = TTDWithIDSerializer
    
##################################################################
#       TTD RetrieveUpdateDelete-View
##################################################################


class TTDRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = TTD.objects.all()
    serializer_class = TTDWithIDSerializer

    lookup_field = "slug"


##################################################################
#               BDD List-View
##################################################################


class BDDListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ["pm_status", "alternate_name"]
    search_fields = [
        "alternate_name",
        "abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
    ]

    serializer_class = BDDSerializer

    def get_queryset(self):
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        queryset = BDD.objects.all()
        free = self.request.GET.get("free")
        if free:
            used_id = set()
            for i in Project.objects.all():
                if i.equipment_delivery_client > current_datetime:
                    if i.bdd:
                        for j in i.bdd.all():
                            used_id.add(j.id)

            queryset = queryset.exclude(id__in=used_id)

        if warehouse:
            queryset = queryset.filter(location_for_warehouse__slug=warehouse)
        return queryset


###################################################################
#              BDD Create-View
###################################################################


class BDDCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = BDD.objects.all()
    serializer_class = BDDCreateSerializer


###################################################################
#              BDD RetUpdDel-RetUpdDelView
###################################################################


class BDDRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = BDD.objects.all()
    serializer_class = BDDCreateSerializer

    lookup_field = "slug"


###################################################################
#              CALIBRATION_STAND List-View
###################################################################


class CalibrationStandListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ["pm_status"]
    search_fields = [
        "alternate_name",
        "abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
    ]

    serializer_class = CalibrationStandSerializer

    def get_queryset(self):
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        queryset = CALIBRATION_STAND.objects.all()
        free = self.request.GET.get("free")
        if free:
            used_id = set()
            for i in Project.objects.all():
                if i.equipment_delivery_client > current_datetime:
                    if i.calibration_stand:
                        for j in i.calibration_stand.all():
                            used_id.add(j.id)

            queryset = queryset.exclude(id__in=used_id)

        if warehouse:
            queryset = queryset.filter(location_for_warehouse__slug=warehouse)
        return queryset


###################################################################
#              CALIBRATION_STAND Create-View
###################################################################


class CalibrationStandCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = CALIBRATION_STAND.objects.all()
    serializer_class = CalibrationCreUpdStandSerializer


###################################################################
#              CALIBRATION_STAND RetUpdDelView
###################################################################


class CalibrationRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = CALIBRATION_STAND.objects.all()
    serializer_class = CalibrationCreUpdStandSerializer
    lookup_field = "slug"


###################################################################
#              SwabMaster List-View
###################################################################


class SwabMasterListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ["pm_status"]
    search_fields = [
        "alternate_name",
        "abbreviation",
        "serial_number",
        "asset_number",
        "packaging",
    ]

    serializer_class = SwabMasterSerializer

    def get_queryset(self):
        warehouse = self.request.query_params.get(
            "warehouse"
        )  # Get the warehouse ID from the request query parameters
        queryset = SwabMaster.objects.all()

        if warehouse:
            queryset = queryset.filter(location_for_warehouse__slug=warehouse)
        return queryset


###################################################################
#              SwabMaster Create-View
###################################################################


class SwabMasterCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = SwabMaster.objects.all()
    serializer_class = SwabMasterCreUpdSerializer


###################################################################
#              SwabMaster RetUpdDel-View
###################################################################


class SwabMasterRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = SwabMaster.objects.all()
    serializer_class = SwabMasterCreUpdSerializer

    lookup_field = "slug"


###################################################################
#              Warehouse-ListView
###################################################################


class WarehouseListView(generics.ListAPIView):
    pagination_class = CustomPagination
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


###################################################################
#              Warehouse-ListView Without Pagination
###################################################################


class WarehouseListViewWP(generics.ListAPIView):
    # pagination_class = CustomPagination
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializerWP


###################################################################
#              Warehouse-CrerateView
###################################################################


class WarehouseCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Warehouse.objects.all()
    serializer_class = WarhouseCreateSerializer


###################################################################
#              Warehouse-RetUpdDel-View
###################################################################


class WarehouseRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseNewListView(generics.RetrieveAPIView):
    pagination_class = CustomPagination
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes = [JWTAuthentication]

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseNewSerializer
