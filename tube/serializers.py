from rest_framework import serializers
from .models import Warehouse
from rest_framework.decorators import api_view
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField
from datetime import datetime
import pytz
from project.models import Project
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

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


from equipment.serializers import (
    TTDWithIDSerializer,
    CalibrationStandSerializer,
    SwabMasterSerializer,
    BDDSerializer,
)
from equipment.models import TTD, BDD, CALIBRATION_STAND, SwabMaster
from equipment.serializers import TTDSerializers


class WarehouseEquipSerializer(serializers.Serializer):
    """
    This Serializer accepts id as slug for warehouse. Provide the `id= <slug of that warehouse>`


    """

    ttd = serializers.SerializerMethodField()
    bdd = serializers.SerializerMethodField()
    calibration_stand = serializers.SerializerMethodField()
    swab_master = serializers.SerializerMethodField()
    location_for_warehouse = serializers.SerializerMethodField()

    def get_ids(
        self,
        date_obj,
        ttds: int = None,
        bdds: int = None,
        calis: int = None,
        swabs: int = None,
    ) -> set:
        """
        Retrieve sets of IDs based on specified criteria.

        Args:
            date_obj: A date object representing the target date for comparison.
            ttds: An optional integer flag (0 or 1) indicating whether to retrieve TTD IDs.
                Default is None.
            bdds: An optional integer flag (0 or 1) indicating whether to retrieve BDD IDs.
                Default is None.
            calis: An optional integer flag (0 or 1) indicating whether to retrieve CALI IDs.
                Default is None.
            swabs: An optional integer flag (0 or 1) indicating whether to retrieve SWAB IDs.
                Default is None.

        Returns:
            A set of matching IDs based on the specified criteria. If multiple flags are set to 1,
            the IDs for the corresponding criteria will be returned.

        Raises:
            Any exceptions that may occur during the execution of the method.

        Example usage:
            ids = get_ids(date_obj, ttds=1)  # Retrieve TTD IDs for the specified date

        Note:
            This method queries the Project model to retrieve sets of IDs based on the given criteria.
            It compares the equipment delivery client date of each project with the provided date_obj
            to determine the matching projects. Depending on the flags provided, it retrieves and returns
            the IDs for the TTD, BDD, CALI, and/or SWAB criteria.
        """

        if date_obj:
            ttd = set()
            bdd = set()
            cali = set()
            swab = set()
            p_qs = Project.objects.all()
            for p in p_qs:
                if p.equipment_delivery_client > date_obj:
                    for t in p.ttd.all():
                        ttd.add(t.id)
                    for b in p.bdd.all():
                        bdd.add(b.id)
                    for s in p.swabmaster_equip.all():
                        swab.add(s.id)
                    for c in p.calibration_stand.all():
                        cali.add(c.id)

            if ttds == 1:
                return ttd
            if bdds == 1:
                return bdd
            if calis == 1:
                return cali
            if swabs == 1:
                return swab

    def get_ttd(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = TTD.objects.all()
        search = str(request.query_params.get("search"))
        date_str = request.GET.get("date")

        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)

        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)

        if search != "None":
            query = Q()

            query |= Q(abbreviation__icontains=search)
            query |= Q(alternate_name__icontains=search)
            query |= Q(serial_number__icontains=search)
            query |= Q(asset_number__icontains=search)
            query |= Q(packaging__icontains=search)
            qs = qs.filter(query)

        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

            ids = self.get_ids(date_obj, ttds=1)
            # print('ttd ids :',ids)
            qs = qs.exclude(id__in=ids)

        serializer = TTDSerializers(qs, many=True)
        return serializer.data

    def get_bdd(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = BDD.objects.all()
        search = str(request.query_params.get("search"))
        date_str = request.GET.get("date")

        if search != "None":
            query = Q()

            query |= Q(abbreviation__icontains=search)
            query |= Q(alternate_name__icontains=search)
            query |= Q(serial_number__icontains=search)
            query |= Q(asset_number__icontains=search)
            query |= Q(packaging__icontains=search)
            qs = qs.filter(query)

        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)

        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)

        if date_str:
            print("date ran")
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

            ids = self.get_ids(date_obj, bdds=1)
            print(" bdd ids :", ids)
            qs = qs.exclude(id__in=ids)

        serializer = BDDSerializer(qs, many=True)
        return serializer.data

    def get_calibration_stand(self, obj):
        request = self.context.get("request")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = CALIBRATION_STAND.objects.all()
        slug = request.query_params.get("slug")
        search = str(request.query_params.get("search"))
        date_str = request.GET.get("date")

        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)
            print(qs)
        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)

        if search != "None":
            query = Q()

            query |= Q(abbreviation__icontains=search)
            query |= Q(alternate_name__icontains=search)
            query |= Q(serial_number__icontains=search)
            query |= Q(asset_number__icontains=search)
            query |= Q(packaging__icontains=search)

            qs = qs.filter(query)

        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

            ids = self.get_ids(date_obj, calis=1)
            print("cali ids :", ids)
            qs = qs.exclude(id__in=ids)

        serializer = CalibrationStandSerializer(qs, many=True)

        return serializer.data

    def get_swab_master(self, obj):
        request = self.context.get("request")
        pm_status = str(request.query_params.get("pm_status")).upper()

        qs = SwabMaster.objects.all()
        slug = request.query_params.get("slug")
        search = str(request.query_params.get("search"))
        date_str = request.GET.get("date")

        if search != "None":
            query = Q()

            query |= Q(abbreviation__icontains=search)
            query |= Q(alternate_name__icontains=search)
            query |= Q(serial_number__icontains=search)
            query |= Q(asset_number__icontains=search)
            query |= Q(packaging__icontains=search)
            qs = qs.filter(query)
        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)

        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)

        if date_str:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

            ids = self.get_ids(date_obj, swabs=1)
            print("swab ids :", ids)
            qs = qs.exclude(id__in=ids)
        serializer = SwabMasterSerializer(qs, many=True)

        return serializer.data
