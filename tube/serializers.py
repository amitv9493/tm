from rest_framework import serializers
from .models import Warehouse
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField
from datetime import datetime
import pytz
from project.models import Project
from django.utils import timezone
from django.db.models import Q, F
from equipment.serializers import (
    CalibrationStandSerializer,
    SwabMasterSerializer,
    BDDSerializer,
)
from core.serializers import DynamicModelSerializer
from equipment.models import TTD, BDD, CALIBRATION_STAND, SwabMaster
from equipment.serializers import TTDSerializers


class WarehouseSerializer(CountryFieldMixin, DynamicModelSerializer):
    country = CountryField(country_dict=True)

    class Meta:
        model = Warehouse
        fields = "__all__"


class WarehouseOptionsSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class WarehouseAvailableSerializer(CountryFieldMixin, serializers.ModelSerializer):
    ttd = serializers.SerializerMethodField()
    bdd = serializers.SerializerMethodField()
    calibration_stand = serializers.SerializerMethodField()
    swabmaster = serializers.SerializerMethodField()
    # parts
    general_part_data = serializers.SerializerMethodField()
    supply_orifice = serializers.SerializerMethodField()
    pressure_sensor = serializers.SerializerMethodField()
    calibration_orifice = serializers.SerializerMethodField()
    swabmasterTSR = serializers.SerializerMethodField()
    devicehose = serializers.SerializerMethodField()
    airhose = serializers.SerializerMethodField()
    ttd_rack = serializers.SerializerMethodField()
    bdd_rack = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Warehouse

    def get_calibration_stand(self, obj):
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = timezone.now().date()
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

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

    def get_bdd_rack(self, obj):
        used = 0
        not_used = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.bdd_rack:
                total = warehouse.bdd_rack.count()
                for j in warehouse.bdd_rack.all():
                    try:
                        if j.TTD:
                            used += 1
                    except:
                        not_used += 1

        return {
            "used": used,
            "not_used": not_used,
            "total": total,
        }
        pass

    def get_ttd_rack(self, obj):
        used = 0
        not_used = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.ttd_rack:
                total = warehouse.ttd_rack.count()
                for j in warehouse.ttd_rack.all():
                    try:
                        if j.TTD:
                            used += 1
                    except:
                        not_used += 1

        return {
            "used": used,
            "not_used": not_used,
            "total": total,
        }

    def get_airhose(self, obj):
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.airhose:
                total = warehouse.airhose.count()
                for j in warehouse.airhose.all():
                    if j.projects:
                        for k in j.projects.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }

    def get_devicehose(self, obj):
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.devicehose:
                total = warehouse.devicehose.count()
                for j in warehouse.devicehose.all():
                    if j.projects:
                        for k in j.projects.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }

    def get_swabmasterTSR(self, obj):
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.swabmasterTSR:
                total = warehouse.swabmasterTSR.count()
                for j in warehouse.swabmasterTSR.all():
                    if j.projects:
                        for k in j.projects.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }

    def get_calibration_orifice(self, obj):
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.calibration_orifice:
                total = warehouse.calibration_orifice.count()
                for j in warehouse.calibration_orifice.all():
                    if j.projects:
                        for k in j.projects.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }

    def get_pressure_sensor(self, obj):
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.supply_orifice:
                total = warehouse.pressure_sensor.count()
                for j in warehouse.pressure_sensor.all():
                    if j.projects:
                        for k in j.projects.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }

    def get_supply_orifice(self, obj):
        will_not_free = 0
        will_be_free = 0
        not_assigned_to_any_project = 0
        total = 0
        request = self.context.get("request")
        warehouse_id = request.query_params.get("id")
        current_datetime = datetime.now(pytz.timezone("Asia/Kolkata")).date()

        if warehouse_id:
            warehouse = Warehouse.objects.get(id=warehouse_id)
            if warehouse.supply_orifice:
                total = warehouse.supply_orifice.count()
                for j in warehouse.supply_orifice.all():
                    if j.projects:
                        for k in j.projects.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }

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

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

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

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

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

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

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

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }

    def get_swabmaster(self, obj):
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
                    if j.Swabmaster:
                        for k in j.Swabmaster.all():
                            if k.equipment_delivery_tubemaster < current_datetime:
                                will_be_free += 1
                            else:
                                will_not_free += 1

            not_assigned_to_any_project = total - (will_not_free + will_be_free)

        return {
            "will_not_free": will_not_free,
            "will_be_free": will_be_free,
            "not_assigned_to_any_project": not_assigned_to_any_project,
            "total": total,
        }
        
        