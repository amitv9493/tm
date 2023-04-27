from rest_framework import serializers
from .models import *



class WarehouseLocationSerializer(serializers.Field):
    def to_representation(self, value):
        if value is not None:
            return value.name
        return None

class SupplyOrificeSerializer(serializers.ModelSerializer):
    location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = Supply_orifice
        fields = "__all__"