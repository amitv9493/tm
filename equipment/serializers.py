from rest_framework import serializers
from rest_framework.fields import empty
from .models import *
from tube.models import *
from part.models import *
from rest_framework import serializers
from datetime import datetime
import pytz
from django_countries import countries
from project.validators import SerialValidator
from django.utils import timezone

##################################################################
#       TTD Serializer
##################################################################


class CustomCountryField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return data


# class TTDLocSerializers(serializers.ModelSerializer):
# 	class Meta:
# 		model = Warehouse
# 		# fields = ["id", "official_name", "country"]
# 		# fields = "_all_"
# 		fields = ['warehouse_name']
# 		read_only_fields = ['warehouse_name']

# 	def to_representation(self, instance):
# 		return instance.warehouse_name


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTD
        fields = [
            "id",
            "alternate_name",
        ]


class TTDSerializers(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()
    supply_orifice_set = serializers.StringRelatedField()
    pressure_sensor = serializers.SerializerMethodField()
    TTD_tube_seal_rack = serializers.StringRelatedField()

    project_slug = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    


    class Meta:
        model = TTD
        fields = (
            "id",
            "abbreviation",
            "alternate_name",
            "serial_number",
            "asset_number",
            "remarks",
            "location_for_warehouse",
            "pm_status",
            "location_for_storage",
            "packaging",
            "if_yes_how_many_in_a_set",
            "supply_orifice_set",
            "pressure_sensor",
            "TTD_tube_seal_rack",
            "frame",
            "image",
            "slug",
            "status",
            "project_slug",
        )
        # depth = 1

    def get_project_slug(self, obj):
        current_datetime = timezone.now().date()  # .values_list("id", flat=True))
        projects = obj.ttd.all().filter(equipment_delivery_client__gt=current_datetime)
        return projects[0].slug if projects else None

    def get_status(self, obj):
        x = self.get_project_slug(obj)
        return 1 if x else None
    
    def get_pressure_sensor(self, obj):
        return obj.pressure_sensor.range if obj.pressure_sensor else None

class TTDWithIDSerializer(serializers.ModelSerializer):
    project_ids = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = TTD
        fields = "__all__"
        read_only_fields = ['slug']

    def get_project_ids(self, obj):
        current_datetime = datetime.now(
            pytz.timezone("Asia/Kolkata")
        ).date()  # .values_list("id", flat=True))
        projects_id = list(
            obj.ttd.all()
            .filter(equipment_delivery_client__gt=current_datetime)
            .values_list("id", flat=True)
        )

        return projects_id[0] if projects_id else None

    def get_status(self, obj):
        x = self.get_project_ids(obj)
        return 1 if x else None
    
    
    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        return super().validate(data)
##################################################################
#       BDD Serializer
##################################################################


class BDDSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()
    BDD_tube_seal_rack = serializers.StringRelatedField()
    status = serializers.SerializerMethodField()
    project_ids = serializers.SerializerMethodField()

    class Meta:
        model = BDD
        fields = "__all__"

    def get_project_ids(self, obj):
        current_datetime = datetime.now(
            pytz.timezone("Asia/Kolkata")
        ).date()  # .values_list("id", flat=True))
        projects_id = list(
            obj.bdd.all()
            .filter(equipment_delivery_client__gt=current_datetime)
            .values_list("id", flat=True)
        )

        return projects_id[0] if projects_id else None

    def get_status(self, obj):
        x = self.get_project_ids(obj)
        return 1 if x else None


##################################################################
#       BDDUpload Serializer
##################################################################


class BDDCreateSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    project_ids = serializers.SerializerMethodField()

    class Meta:
        model = BDD
        fields = "__all__"
        read_only_fields = ['slug']

    def get_project_ids(self, obj):
        current_datetime = datetime.now(
            pytz.timezone("Asia/Kolkata")
        ).date()  # .values_list("id", flat=True))
        projects_id = list(
            obj.bdd.all()
            .filter(equipment_delivery_client__gt=current_datetime)
            .values_list("id", flat=True)
        )

        return projects_id[0] if projects_id else None

    def get_status(self, obj):
        x = self.get_project_ids(obj)
        return 1 if x else None


    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        return super().validate(data)
##################################################################
#       CALIBRATION_STAND Serializer
##################################################################


class CalibrationStandSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()
    calibration_orifice_set = serializers.StringRelatedField()
    status = serializers.SerializerMethodField()
    project_ids = serializers.SerializerMethodField()

    class Meta:
        model = CALIBRATION_STAND
        fields = "__all__"

    def get_project_ids(self, obj):
        current_datetime = datetime.now(
            pytz.timezone("Asia/Kolkata")
        ).date()  # .values_list("id", flat=True))
        projects_id = list(
            obj.calibration_stand.all()
            .filter(equipment_delivery_client__gt=current_datetime)
            .values_list("id", flat=True)
        )

        return projects_id[0] if projects_id else None

    def get_status(self, obj):
        x = self.get_project_ids(obj)
        return 1 if x else None


##################################################################
#       CALIBRATION_STANDCreUpd Serializer
##################################################################


class CalibrationCreUpdStandSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    project_ids = serializers.SerializerMethodField()

    class Meta:
        model = CALIBRATION_STAND
        fields = "__all__"
        read_only_fields = ['slug']

    def get_project_ids(self, obj):
        current_datetime = datetime.now(
            pytz.timezone("Asia/Kolkata")
        ).date()  # .values_list("id", flat=True))
        projects_id = list(
            obj.calibration_stand.all()
            .filter(equipment_delivery_client__gt=current_datetime)
            .values_list("id", flat=True)
        )

        return projects_id[0] if projects_id else None

    def get_status(self, obj):
        x = self.get_project_ids(obj)
        return 1 if x else None


    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        return super().validate(data)
##################################################################
#       SwabMaster Serializer
##################################################################


class SwabMasterSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()
    Swab_Master_Tube_Seal_Rack = serializers.StringRelatedField()
    status = serializers.SerializerMethodField()
    project_ids = serializers.SerializerMethodField()

    class Meta:
        model = SwabMaster
        fields = "__all__"

    def get_project_ids(self, obj):
        current_datetime = datetime.now(
            pytz.timezone("Asia/Kolkata")
        ).date()  # .values_list("id", flat=True))
        projects_id = list(
            obj.Swabmaster.all()
            .filter(equipment_delivery_client__gt=current_datetime)
            .values_list("id", flat=True)
        )

        return projects_id[0] if projects_id else None

    def get_status(self, obj):
        x = self.get_project_ids(obj)
        return 1 if x else None


##################################################################
#       SwabMasterCreUpd Serializer
##################################################################


class SwabMasterCreUpdSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    project_ids = serializers.SerializerMethodField()

    class Meta:
        model = SwabMaster
        fields = "__all__"
        read_only_fields = ['slug']

    class Meta:
        model = SwabMaster
        fields = "__all__"

    def get_project_ids(self, obj):
        current_datetime = datetime.now(
            pytz.timezone("Asia/Kolkata")
        ).date()  # .values_list("id", flat=True))
        projects_id = list(
            obj.Swabmaster.all()
            .filter(equipment_delivery_client__gt=current_datetime)
            .values_list("id", flat=True)
        )

        return projects_id[0] if projects_id else None

    def get_status(self, obj):
        x = self.get_project_ids(obj)
        return 1 if x else None


    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        
        return super().validate(data)

##################################################################
#       Warehouse Serializer
##################################################################


class WarehouseSerializer(serializers.ModelSerializer):
    country = CustomCountryField()

    class Meta:
        model = Warehouse
        fields = "__all__"


##################################################################
#       Warehouse Serializer Without pagination and get id and name only
##################################################################


class WarehouseSerializerWP(serializers.ModelSerializer):
    # country = CustomCountryField()

    class Meta:
        model = Warehouse
        fields = ("id", "warehouse_name")


##################################################################
#       Warehouse Create-Serializer
##################################################################


class WarhouseCreateSerializer(serializers.ModelSerializer):
    country = CustomCountryField()

    class Meta:
        model = Warehouse
        fields = "__all__"


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = (
            "id",
            "part_name",
        )


class WarehouseNewSerializer(serializers.ModelSerializer):
    # country = CustomCountryField()
    parts = serializers.SerializerMethodField()
    TTD = serializers.SerializerMethodField()
    BDD = serializers.SerializerMethodField()
    Calibration_Stand = serializers.SerializerMethodField()
    SwabMaster = serializers.SerializerMethodField()
    supply_orifice = serializers.SerializerMethodField()
    pressure_sensor = serializers.SerializerMethodField()
    ttd_rack = serializers.SerializerMethodField()
    bdd_rack = serializers.SerializerMethodField()
    calibration_orifice = serializers.SerializerMethodField()
    swabmasterTSR = serializers.SerializerMethodField()
    devicehose = serializers.SerializerMethodField()
    airhose = serializers.SerializerMethodField()

    # equipments = serializers.SerializerMethodField()
    class Meta:
        model = Warehouse
        fields = (
            "parts",
            "TTD",
            "BDD",
            "Calibration_Stand",
            "SwabMaster",
            "supply_orifice",
            "pressure_sensor",
            "ttd_rack",
            "bdd_rack",
            "calibration_orifice",
            "swabmasterTSR",
            "devicehose",
            "airhose",
        )

    def get_parts(self, obj):
        return obj.part.all().count()

    def get_TTD(self, obj):
        return obj.ttd.all().count()

    def get_BDD(self, obj):
        return obj.bdd.all().count()

    def get_Calibration_Stand(self, obj):
        return obj.calibration_stand.all().count()

    def get_SwabMaster(self, obj):
        return obj.swabmaster.all().count()

    def get_supply_orifice(self, obj):
        return obj.supply_orifice.all().count()

    def get_pressure_sensor(self, obj):
        return obj.pressure_sensor.all().count()

    def get_ttd_rack(self, obj):
        return obj.ttd_rack.all().count()

    def get_bdd_rack(self, obj):
        return obj.bdd_rack.all().count()

    def get_calibration_orifice(self, obj):
        return obj.calibration_orifice.all().count()

    def get_swabmasterTSR(self, obj):
        return obj.swabmasterTSR.all().count()

    def get_devicehose(self, obj):
        return obj.devicehose.all().count()

    def get_airhose(self, obj):
        return obj.airhose.all().count()
