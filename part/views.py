from rest_framework import generics
from rest_framework.permissions import  DjangoModelPermissions, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .serializers import *
from tm_api.paginator import CustomPagination
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
    authentication_classes= [JWTAuthentication]
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
        so = set()
        
        if ttd_id:
            for ttd in TTD.objects.exclude(id = ttd_id):
                if ttd.supply_orifice_set:
                    so.add(ttd.supply_orifice_set.id)

        else:
            for ttd in TTD.objects.all():
                if ttd.supply_orifice_set:
                    so.add(ttd.supply_orifice_set.id)
                    
        qs = Supply_orifice.objects.exclude(id__in=so)
            
        return qs


    





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
        pressure_sensor = set()
        if ttd_id:
            for ttd in TTD.objects.exclude(id=ttd_id):
                if ttd.pressure_sensor:
                    pressure_sensor.add(ttd.pressure_sensor.id)
                
        else:
            for ttd in TTD.objects.all():
                if ttd.pressure_sensor:
                    pressure_sensor.add(ttd.pressure_sensor.id)

        qs = qs.exclude(id__in = pressure_sensor)
        return qs


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
        if ttd_id:
            so = set()
            for ttd in TTD.objects.exclude(id=ttd_id):
                if ttd.TTD_tube_seal_rack:
                    so.add(ttd.TTD_tube_seal_rack.id)
            qs= TTD_tube_seal_rack.objects.exclude(id__in=so)

        else:
            for ttd in TTD.objects.all():
                if ttd.TTD_tube_seal_rack:
                    so.add(ttd.TTD_tube_seal_rack.id)
            
        qs= TTD_tube_seal_rack.objects.exclude(id__in=so)
        return qs


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
        bdd_id = self.request.GET.get('bdd_id')
        so = set()
        
        if bdd_id:
            for bdd in BDD.objects.exclude(id=bdd_id):
                if bdd.BDD_tube_seal_rack:
                    so.add(bdd.BDD_tube_seal_rack.id)
        else:
            for bdd in BDD.objects.all():
                if bdd.BDD_tube_seal_rack:
                    so.add(bdd.BDD_tube_seal_rack.id)
        
        qs = BDD_tube_seal_rack.objects.exclude(id__in = so)
        return qs

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
        swab_id = self.request.GET.get('swab_id')
        
        if swab_id:
            swabmaster_id = set()
            for swab in SwabMaster.objects.exclude(id=swab_id):
                if swab.Swab_Master_Tube_Seal_Rack:
                    swabmaster_id.add(swab.Swab_Master_Tube_Seal_Rack.id)
            qs = SwabMasterTSR.objects.exclude(id__in = swabmaster_id)
            return qs
        else:
            return qs

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
    queryset = AirHose.objects.all()


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
        so = set()
        
        if cr_id:
            for cr in CALIBRATION_STAND.objects.exclude(id = cr_id):
                if cr.calibration_orifice_set:
                    so.add(cr.calibration_orifice_set.id)

        else:
            for cr in CALIBRATION_STAND.objects.all():
                if cr.calibration_orifice_set:
                    so.add(cr.calibration_orifice_set.id)
                    
        qs = Calibration_orifice.objects.exclude(id__in=so)
            
        return qs
    
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

class AirHoseRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = AirHoseCreSerializer
    queryset = AirHose.objects.all()

#######################################################################
#                     DeviceHose-ListView 
#######################################################################

class DeviceHoseRListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = DeviceHoseListSerializer
    queryset = DeviceHose.objects.all()

#######################################################################DeviceHoseRListView
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

#######################################################################
#                     SwabMaster-ListView 
#######################################################################

class SwabMasterTSRListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = SwabMasterTSRSerializer
    queryset = SwabMasterTSR.objects.all()

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

class SwabMasterTSRRetUpdDelViewl(generics.ListCreateAPIView):
    ermission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = SwabMasterTSRCreateSerializer
    queryset = SwabMasterTSR.objects.all()

#######################################################################
#                     CalibrationOrifice-ListView 
#######################################################################

class CalibrationOrificeListView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    serializer_class = CalibratiobOrificeSerializer
    queryset = Calibration_orifice.objects.all()

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
    
#######################################################################
#                     BddTubesealrack-ListViewView 
#######################################################################

class BddTubesealrackList(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    pagination_class = CustomPagination
    serializer_class = BddTubesealrackListSerializer
    queryset = BDD_tube_seal_rack.objects.all()
    

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


#######################################################################
#                     TddTubesealrack-ListViewView 
#######################################################################

class TddTubesealrackList(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]

    serializer_class = TddTubesealrackListSerializer
    queryset = TTD_tube_seal_rack.objects.all()

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

#######################################################################
#                     PressureSensor-ListView 
#######################################################################

class PressureSensorListView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    authentication_classes = [JWTAuthentication]
    

    serializer_class = PressuresensorListSerializer
    queryset = Pressure_sensor.objects.all()  

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