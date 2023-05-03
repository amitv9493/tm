from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication


##################################################################
#       TTD List-View
##################################################################


class TTDListView(ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

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
    serializer_class = TTDSerializers


##################################################################
#               BDD List-View
##################################################################


class BDDListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

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

class SwabMasterView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    queryset = SwabMaster.objects.all()
    serializer_class = SwabMasterSerializer

