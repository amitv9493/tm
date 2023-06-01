from rest_framework import serializers
from .models import *


################################################################################
#                SupplySerializer
################################################################################


class SupplyOrificeSerializer(serializers.ModelSerializer):
    # location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = Supply_orifice
        fields = "__all__"

################################################################################
#                PressureSensorSerializer
################################################################################


class PressureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure_sensor
        fields = "__all__"

################################################################################
#                TTD_tube_seal_rack Serializer
################################################################################

class TTDTubeSealRackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTD_tube_seal_rack
        fields = "__all__"
        # depth = 1

################################################################################
#                BDD_tube_seal_rack Serializer
################################################################################

class BDDTubeSealRackSerializer(serializers.ModelSerializer):    
    class Meta:
        model = BDD_tube_seal_rack
        fields = "__all__"


################################################################################
#                SwabMaster Serializer
################################################################################


class SwabMasterTSRSerializer(serializers.ModelSerializer):    
    location_for_warehouse = serializers.StringRelatedField() 
    class Meta:
        model = SwabMasterTSR
        fields = "__all__"


################################################################################
#                DeviceHose Serializer
################################################################################


class DeviceHoseSerializer(serializers.ModelSerializer):    
    class Meta:
        model = DeviceHose
        fields = "__all__"


################################################################################
#                AirHose Serializer
################################################################################


class AirHoseSerializer(serializers.ModelSerializer):  
    warehouse = serializers.StringRelatedField()  
    class Meta:
        model = AirHose
        fields = "__all__"

################################################################################
#                Calibration Serializer
################################################################################


class Calibration_orifice_serializer(serializers.ModelSerializer):    
    class Meta:
        model = Calibration_orifice
        fields = "__all__"

################################################################################
#                AirHose Serializer
################################################################################

class AirHoseCreSerializer(serializers.ModelSerializer):   
    location_for_warehouse = serializers.StringRelatedField() 
    class Meta:
        model = AirHose
        fields = "__all__"

################################################################################
#                DeviseHose Serializer
################################################################################

class DeviceHoseListSerializer(serializers.ModelSerializer):
    warehouse = serializers.StringRelatedField() 
    class Meta:
        model = DeviceHose
        fields = "__all__"

################################################################################
#                DeviseHose Serializer
################################################################################

class DeviceHoseCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceHose
        fields = "__all__"

################################################################################
#                Swabmastertsr Serializer
################################################################################

class SwabMasterTSRCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwabMasterTSR
        fields = "__all__"

################################################################################
#                CalibrationOrifice Serializer
################################################################################

class CalibratiobOrificeSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField() 
    class Meta:
        model = Calibration_orifice
        fields = "__all__"

################################################################################
#                CalibrationOrificeCreate Serializer
################################################################################

class CalibratiobOrificeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibration_orifice
        fields = "__all__"

################################################################################
#                BddTubesealrackList Serializer
################################################################################

class BddTubesealrackListSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField() 
    class Meta:
        model = BDD_tube_seal_rack
        fields = "__all__"

################################################################################
#                BddTubesealrackCreate Serializer
################################################################################

class BddTubesealrackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BDD_tube_seal_rack
        fields = "__all__"       

################################################################################
#                TddTubesealrackList Serializer
################################################################################

class TddTubesealrackListSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField() 
    class Meta:
        model = TTD_tube_seal_rack
        fields = "__all__"

################################################################################
#                TddTubesealrackCreate Serializer
################################################################################

class TddTubesealrackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTD_tube_seal_rack
        fields = "__all__"  

################################################################################
#                PressuresensorList Serializer
################################################################################

class PressuresensorListSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField() 
    class Meta:
        model = Pressure_sensor
        fields = "__all__"

################################################################################
#                PressuresensorCreate Serializer
################################################################################

class PressuresensorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure_sensor
        fields = "__all__"

################################################################################
#                SupplyOrificeList Serializer
################################################################################

class SupplyOrificeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply_orifice
        fields = "__all__"

################################################################################
#                SupplyOrificeCreate Serializer
################################################################################

class SupplyOrificeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply_orifice
        fields = "__all__"

################################################################################
#                AllGeneralPartList Serializer
################################################################################

class AllGeneralPartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = "__all__"
        

################################################################################
#                AllGeneralPartCreate Serializer
################################################################################

class AllGeneralPartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = "__all__"
        
class WarehousePartSerializer(serializers.Serializer):
    general_part = serializers.SerializerMethodField()
    supply_orifice = serializers.SerializerMethodField()
    pressure_sensor = serializers.SerializerMethodField()
    ttd_rack = serializers.SerializerMethodField()
    bdd_rack = serializers.SerializerMethodField()
    calibration_orifice = serializers.SerializerMethodField()
    swabmasterTSR = serializers.SerializerMethodField()
    devicehose = serializers.SerializerMethodField()
    airhose = serializers.SerializerMethodField()
    
    def get_general_part(self, obj):
        request = self.context.get('request')
        id = request.query_params.get('id')
        if id:
            qs = Part.objects.filter(location_for_warehouse = id)
            
            serializer = AllGeneralPartCreateSerializer(qs, many=True)
            return serializer.data

    def get_supply_orifice(self, obj):
        request = self.context.get('request')
        id = request.query_params.get('id')
        if id:
            qs = Supply_orifice.objects.filter(location_for_warehouse = id)
            
            serializer = SupplyOrificeCreateSerializer(qs, many=True)
            return serializer.data

    def get_pressure_sensor(self, obj):
        request = self.context.get('request')
        id = request.query_params.get('id')
        if id:
            qs = Pressure_sensor.objects.filter(location_for_warehouse = id)
            
            serializer = SupplyOrificeCreateSerializer(qs, many=True)
            return serializer.data 
    
    def get_ttd_rack(self, obj):
        request = self.context.get('request')
        id = request.query_params.get('id')
        if id:
            qs = TTD_tube_seal_rack.objects.filter(location_for_warehouse = id)
            
            serializer = TddTubesealrackCreateSerializer(qs, many=True)
            return serializer.data
        
    def get_bdd_rack(self, obj):
        request = self.context.get('request')
        id = request.query_params.get('id')
        if id:
            qs = BDD_tube_seal_rack.objects.filter(location_for_warehouse = id)
            
            serializer = BDDTubeSealRackSerializer(qs, many=True)
            return serializer.data

    def get_calibration_orifice(self,obj):
        request = self.context.get('request')
        id = request.query_params.get('id')
        if id:
            qs = Calibration_orifice.objects.filter(location_for_warehouse = id)
            
            serializer = Calibration_orifice_serializer(qs, many=True)
            return serializer.data
    
    def get_swabmasterTSR(self, obj):
        request = self.context.get('request')
        id = request.query_params.get('id')
        if id:
            qs = SwabMasterTSR.objects.filter(location_for_warehouse = id)
            
            serializer = SwabMasterTSRSerializer(qs, many=True)
            return serializer.data
    
    def get_devicehose(self, obj):
        request = self.context.get('request')
        id = request.query_params.get('id')
        if id:
            qs = DeviceHose.objects.filter(warehouse = id)
            
            serializer = DeviceHoseSerializer(qs, many=True)
            return serializer.data
    
    def get_airhose(self, obj):
        request = self.context.get('request')
        id = request.query_params.get('id')
        if id:
            qs = AirHose.objects.filter(warehouse = id)
            
            serializer = AirHoseSerializer(qs, many=True)
            return serializer.data