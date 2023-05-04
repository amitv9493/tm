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
        
###############################################################
#          Plant-Serializers
###############################################################
from django_countries.serializer_fields import CountryField as DjangoCountryField

class CountryField(DjangoCountryField):
    def to_representation(self, value):
        return value.code

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("official_name",)

class PlantSerializers(serializers.ModelSerializer):
    client = ClientSerializer()
    country = CountryField(default="")
    class Meta:
        model = Plant
        fields = "__all__"



