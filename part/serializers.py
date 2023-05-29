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
    class Meta:
        model = AirHose
        fields = "__all__"

################################################################################
#                DeviseHose Serializer
################################################################################

class DeviceHoseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceHose
        fields = "__all__"