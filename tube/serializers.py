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
    ttd = serializers.SerializerMethodField()
    bdd = serializers.SerializerMethodField()
    swabMaster = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Warehouse


    
    def get_bdd(self, obj):
        
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.ttd:
                total = warehouse.ttd.count()
                for j in warehouse.ttd.all():
                    if j.ttd:
                        for k in j.ttd.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (
                will_not_free + will_be_free
            )

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }


    
    def get_general_part_data(self, obj):
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.part:
                total = warehouse.part.count()
                for j in warehouse.part.all():
                    if j.projects:
                        for k in j.projects.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (
                will_not_free + will_be_free
            )

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }

    def get_ttd(self, obj):

        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.ttd:
                total = warehouse.ttd.count()
                for j in warehouse.ttd.all():
                    if j.ttd:
                        for k in j.ttd.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (
                will_not_free + will_be_free
            )

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }



    def get_calibration_stand(self, obj):
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.calibration_stand:
                total = warehouse.calibration_stand.count()
                for j in warehouse.calibration_stand.all():
                    if j.calibration_stand:
                        for k in j.calibration_stand.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (
                will_not_free + will_be_free
            )

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }


    def get_swabMaster(self, obj):
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.swabmaster:
                total = warehouse.swabmaster.count()
                for j in warehouse.swabmaster.all():
                    if j.swabmaster:
                        for k in j.swabmaster.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (
                will_not_free + will_be_free
            )

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }
