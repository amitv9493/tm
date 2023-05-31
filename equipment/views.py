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
from tm_api.paginator import CustomPagination

##################################################################
#       TTD List-View
##################################################################
class TTDListView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,]
    filterset_fields = ['pm_status','alternate_name', '' ]
    search_fields = [
        'alternate_name',
        'abbreviation',
        'serial_number',
        'asset_number',
        'packaging', 
    ]
    queryset = TTD.objects.all()
    serializer_class = TTDSerializers


##################################################################
#       TTD Create-View
##################################################################


class TTDCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = TTD.objects.all()
    serializer_class = TTDSerializers


##################################################################
#       TTD RetrieveUpdateDelete-View
##################################################################


class TTDRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = TTD.objects.all()
    serializer_class = TTDWithIDSerializer


##################################################################
#               BDD List-View
##################################################################


class BDDListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    queryset = BDD.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,]
    filterset_fields = ['pm_status']
    search_fields = [
        'alternate_name',
        'abbreviation',
        'serial_number',
        'asset_number',
        'packaging',
        
    ]
    serializer_class = BDDSerializer


###################################################################
#              BDD Create-View
###################################################################


class BDDCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = BDD.objects.all()
    serializer_class = BDDSerializer


###################################################################
#              BDD RetUpdDel-RetUpdDelView
###################################################################


class BDDRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = BDD.objects.all()
    serializer_class = BDDSerializer

###################################################################
#              CALIBRATION_STAND List-View
###################################################################

class CalibrationStandListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,]
    filterset_fields = ['pm_status']
    search_fields = [
        'alternate_name',
        'abbreviation',
        'serial_number',
        'asset_number',
        'packaging',
    ]
    queryset = CALIBRATION_STAND.objects.all()
    serializer_class = CalibrationStandSerializer


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
    

###################################################################
#              SwabMaster List-View
###################################################################

class SwabMasterListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,]
    filterset_fields = ['pm_status']
    search_fields = [
        'alternate_name',
        'abbreviation',
        'serial_number',
        'asset_number',
        'packaging',
    ]
    queryset = SwabMaster.objects.all()
    serializer_class = SwabMasterSerializer

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
#              Warehouse-CrerateView
###################################################################

class WarehouseCreateView(generics.CreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


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
