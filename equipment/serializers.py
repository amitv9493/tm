from rest_framework import serializers
from .models import *
from tube.models import *

##################################################################
#       TTD Serializer
##################################################################


class TTDSerializers(serializers.ModelSerializer):
    class Meta:
        model = TTD
        fields = "__all__"
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


from django_countries.serializer_fields import CountryField

class CountrySerializerField(serializers.Field):
    def to_representation(self, value):
        return value.code

class WarehouseSerializer(serializers.ModelSerializer):
    country = CountrySerializerField()

    class Meta:
        model = Warehouse
        fields = "__all__"
