from rest_framework import generics
from rest_framework.permissions import  DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .serializers import *

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
    # permission_classes = [DjangoModelPermissions, IsAdminUser]
    # authentication_classes= [JWTAuthentication]
    serializer_class = SupplyOrificeSerializer

    def get_queryset(self):
        so = set()
        for ttd in TTD.objects.all():
            so.add(ttd.supply_orifice_set.id)
        so_qs = Supply_orifice.objects.exclude(id__in = so)
        return so_qs
    




##################################################################################
#                  PressureSensor View
##################################################################################


class PressureSensorViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = PressureSensorSerializer
    def get_queryset(self):
        so = set()
        for ttd in TTD.objects.all():
            so.add(ttd.pressure_sensor.id)
        so_qs = Pressure_sensor.objects.exclude(id__in = so)
        return so_qs


##################################################################################
#                  TTDTubeSealRack  View
##################################################################################


class TTDTubeSealRackViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = TTDTubeSealRackSerializer
    def get_queryset(self):
        so = set()
        for ttd in TTD.objects.all():
            so.add(ttd.TTD_tube_seal_rack.id)
        so_qs = TTD_tube_seal_rack.objects.exclude(id__in = so)
        return so_qs


##################################################################################
#                  BDDTubeSealRack  View
##################################################################################


class BDDTubeSealRackViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = BDDTubeSealRackSerializer
    queryset = BDD_tube_seal_rack.objects.all()


################################################################################
#                SwabMaster View
################################################################################

class SwabMasterTSRViewPart(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = SwabMasterTSRSerializer
    # queryset = SwabMasterTSR.objects.all()
    def get_queryset(self):
        so = set()
        for swab in SwabMaster.objects.all():
            # if swab.Swab_Master_Tube_Seal_Rack:
                so.add(swab.Swab_Master_Tube_Seal_Rack.id)
        so_qs = SwabMasterTSR.objects.exclude(id__in = so)
        return so_qs

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
    pagination_class = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = AirHoseSerializer
    queryset = AirHose.objects.all()

################################################################################
#                AirHose View
################################################################################


# class 