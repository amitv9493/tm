from rest_framework import serializers
from .models import *
from tube.models import *
from part.models import Part


##################################################################
#       TTD Serializer
##################################################################


class TTDSerializers(serializers.ModelSerializer):
    class Meta:
        model = TTD
        fields = "__all__"
        # depth = 1

class TTDLocSerializers(serializers.ModelSerializer):
    class Meta:
        model = TTD
        fields = "location_for_warehouse"
        # depth = 1


##################################################################
#       BDD Serializer
##################################################################

class BDDSerializer(serializers.ModelSerializer):
    class Meta:
        model = BDD
        fields = "__all__"
        
##################################################################
#       CALIBRATION_STAND Serializer
##################################################################

class CalibrationStandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CALIBRATION_STAND
        fields = "__all__"

##################################################################
#       SwabMaster Serializer
##################################################################

class SwabMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwabMaster
        fields = "__all__"


##################################################################
#       Warehouse Serializer
##################################################################


from rest_framework import serializers
from django_countries import countries

class CustomCountryField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return data

class WarehouseSerializer(serializers.ModelSerializer):
    country = CustomCountryField()

    class Meta:
        model = Warehouse
        fields = "__all__"

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = (
            "id",
            "part_name",
        )
        
class WarehouseNewSerializer(serializers.ModelSerializer):
    # country = CustomCountryField()
    parts = serializers.SerializerMethodField()
    TTD = serializers.SerializerMethodField()
    BDD = serializers.SerializerMethodField()
    Calibration_Stand = serializers.SerializerMethodField()
    SwabMaster = serializers.SerializerMethodField()
    supply_orifice = serializers.SerializerMethodField()
    pressure_sensor = serializers.SerializerMethodField()
    ttd_rack = serializers.SerializerMethodField()
    bdd_rack = serializers.SerializerMethodField()
    calibration_orifice = serializers.SerializerMethodField()
    swabmasterTSR = serializers.SerializerMethodField()
    devicehose = serializers.SerializerMethodField()
    airhose = serializers.SerializerMethodField()
    
    # equipments = serializers.SerializerMethodField()
    class Meta:
        model = Warehouse
        fields = (
            "parts",
            "TTD",
            "BDD",
            "Calibration_Stand",
            "SwabMaster",
            "supply_orifice",
            "pressure_sensor",
            "ttd_rack",
            "bdd_rack",
            "calibration_orifice",
            "swabmasterTSR",
            "devicehose",
            "airhose",
        )


    def get_parts(self, obj):
        return obj.part.all().count()

    def get_TTD(self, obj):
        return obj.ttd.all().count()
    
    def get_BDD(self, obj):
        return obj.bdd.all().count()
        
    
    def get_Calibration_Stand(self, obj):
        return obj.calibration_stand.all().count()
        

    def get_SwabMaster(self, obj):
        return obj.swabmaster.all().count()
        
    def get_supply_orifice(self, obj):
        return obj.supply_orifice.all().count()
        
    def get_pressure_sensor(self, obj):
        return obj.pressure_sensor.all().count()
            
    
    def get_ttd_rack(self, obj):
        return obj.ttd_rack.all().count()
        
    def get_bdd_rack(self, obj):
        return obj.bdd_rack.all().count()
        
    def get_calibration_orifice(self, obj):
        return obj.calibration_orifice.all().count()

    def get_swabmasterTSR(self, obj):
        return obj.swabmasterTSR.all().count()
        
    def get_devicehose(self, obj):
        return obj.devicehose.all().count()

    def get_airhose(self, obj):
        return obj.airhose.all().count()
        
