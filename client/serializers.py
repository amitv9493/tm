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
    client = ClientSerializers()
    country = CountryField(default="")
    official_address = AddressSerializers(many=True)
    shipping_address = AddressSerializers(many=True)
    plantentrance_address = AddressSerializers(many=True)

    class Meta:
        model = Plant
        fields = "__all__"

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        official_address_data = validated_data.pop('official_address')
        shipping_address_data = validated_data.pop('shipping_address')
        plantentrance_address_data = validated_data.pop('plantentrance_address')

        client = Client.objects.create(**client_data)

        plant = Plant.objects.create(client=client, **validated_data)

        for address_data in official_address_data:
            address = Address.objects.create(**address_data)
            plant.official_address.add(address)

        for address_data in shipping_address_data:
            address = Address.objects.create(**address_data)
            plant.shipping_address.add(address)

        for address_data in plantentrance_address_data:
            address = Address.objects.create(**address_data)
            plant.plantentrance_address.add(address)

        return plant

###############################################################
#          PlantUpdate-Serializers
###############################################################

class PlantSerializersupdate(serializers.ModelSerializer):
    country = CountryField(default="")
    # client = ClientSerializers(read_only=True)
    # country = CountryField(default="", read_only=True)
    # official_address = AddressSerializers(many=True, read_only=True)
    # shipping_address = AddressSerializers(many=True, read_only=True)
    # plantentrance_address = AddressSerializers(many=True, read_only=True)

    class Meta:
        model = Plant
        fields = "__all__"

##################################################################
#                Reactor Serializers
##################################################################
        
class ReactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reactor
        fields = "__all__"

##################################################################
#                Unit Serializers
##################################################################

class UnitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


