from rest_framework import serializers
from .models import *


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