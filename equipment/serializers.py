from rest_framework import serializers
from .models import TTD


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
        model = TTD
        fields = "__all__"
        