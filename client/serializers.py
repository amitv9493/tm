from rest_framework import serializers
from .models import *




###############################################################
#          Client Serializers
###############################################################

class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"




