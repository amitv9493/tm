from rest_framework import serializers
from .models import Warehouse
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField


class WarehouseSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country = CountryField(country_dict=True)

    class Meta:
        model = Warehouse
        fields = "__all__"
