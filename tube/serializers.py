from rest_framework import serializers
from .models import Warehouse
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField
from datetime import datetime
import pytz
from django.db.models import Count, Q

class WarehouseSerializer(CountryFieldMixin, serializers.ModelSerializer):
    country = CountryField(country_dict=True)

    class Meta:
        model = Warehouse
        fields = "__all__"


class WarehouseOptionsSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class WarehouseAvailableSerializer(CountryFieldMixin, serializers.ModelSerializer):
    general_part_data = serializers.SerializerMethodField()


    class Meta:
        fields = "__all__"
        model = Warehouse

    def get_general__part_data(self, obj):
        will_not_free_part = 0
        will_be_free_avaialble_part = 0
        not_assigned_to_any_project = 0
        total_parts = 0
        request = self.context.get('request')
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id = warehouse_id)
            if warehouse.part:
                total_parts = warehouse.part.count()
                for j in warehouse.part.all():
                    if j.projects:
                        for k in j.projects.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free_avaialble_part += 1
                            else:
                                will_not_free_part += 1
            
            not_assigned_to_any_project =total_parts - ( will_not_free_part + will_be_free_avaialble_part)
                                
        return {
            'will_not_free_part':will_not_free_part,
            'will_be_free_avaialble_part':will_be_free_avaialble_part,
            'not_assigned_to_any_project':not_assigned_to_any_project,
            'total_parts':total_parts,            
        }
        


class WarehouseAvailableSerializer(CountryFieldMixin, serializers.ModelSerializer):
    general_part_data = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Warehouse

    def get_general_part_data(self, obj):
        request = self.context.get('request')
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        warehouse = Warehouse.objects.filter(id=warehouse_id).prefetch_related('part', 'part__projects').annotate(
            total_parts=Count('part'),
            will_not_free_part=Count('part__projects', filter=Q(part__projects__equipment_delivery_tubemaster__gte=current_datetime)),
            will_be_free_available_part=Count('part__projects', filter=Q(part__projects__equipment_delivery_tubemaster__lt=current_datetime)),
        ).first()
        print(type(warehouse))

        not_assigned_to_any_project = warehouse.total_parts - (warehouse.will_not_free_part + warehouse.will_be_free_available_part)

        return {
            'will_not_free_part': warehouse.will_not_free_part,
            'will_be_free_available_part': warehouse.will_be_free_available_part,
            'not_assigned_to_any_project': not_assigned_to_any_project,
            'total_parts': warehouse.total_parts,
        }





