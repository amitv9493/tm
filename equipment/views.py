from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from tube.models import Warehouse
from django_filters import rest_framework as filters

from tm_api.paginator import CustomPagination

##################################################################
#       TTD List-View
##################################################################
class TTDListView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    filter_backends = [filters.DjangoFilterBackend]
    pagination_class = CustomPagination
    filterset_fields = ('location_for_warehouse',)
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


    queryset = CALIBRATION_STAND.objects.all()
    serializer_class = CalibrationStandSerializer


###################################################################
#              CALIBRATION_STAND Create-View
###################################################################

class CalibrationStandCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = CALIBRATION_STAND.objects.all()
    serializer_class = CalibrationStandSerializer


###################################################################
#              CALIBRATION_STAND RetUpdDelView
###################################################################

class CalibrationRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = CALIBRATION_STAND.objects.all()
    serializer_class = CalibrationStandSerializer
    

###################################################################
#              SwabMaster List-View
###################################################################

class SwabMasterListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = SwabMaster.objects.all()
    serializer_class = SwabMasterSerializer

###################################################################
#              SwabMaster Create-View
###################################################################

class SwabMasterCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = SwabMaster.objects.all()
    serializer_class = SwabMasterSerializer

###################################################################
#              SwabMaster RetUpdDel-View
###################################################################

class SwabMasterRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = SwabMaster.objects.all()
    serializer_class = SwabMasterSerializer

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