from rest_framework import serializers
from .models import *




###############################################################
#          Client Serializers
###############################################################

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


###############################################################
#          Address Serializers
###############################################################

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        


