from rest_framework import serializers

from core.serializers import DynamicModelSerializer
from project.validators import SerialValidator
from tube.serializers import WarehouseSerializer

from .models import *

################################################################################
#                SupplySerializer
################################################################################


class SupplyOrificeSerializer(serializers.ModelSerializer):
    # location_for_warehouse = WarehouseLocationSerializer()
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = Supply_orifice
        fields = "__all__"


################################################################################
#                PressureSensorSerializer
################################################################################


class PressureSensorSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()
    part_type = serializers.SerializerMethodField()

    class Meta:
        model = Pressure_sensor
        fields = "__all__"

    def get_part_type(self, obj):
        return "Pressure sensor"


################################################################################
#                TTD_tube_seal_rack Serializer
################################################################################


class TTDTubeSealRackSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = TTD_tube_seal_rack
        fields = "__all__"
        # depth = 1


################################################################################
#                BDD_tube_seal_rack Serializer
################################################################################


class BDDTubeSealRackSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()
    part_type = serializers.SerializerMethodField()

    class Meta:
        model = BDD_tube_seal_rack
        fields = "__all__"

    def get_part_type(self, obj):
        return "BDD tube seal rack"


################################################################################
#                SwabMaster Serializer
################################################################################


class SwabMasterTSRSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()
    part_type = serializers.StringRelatedField()

    class Meta:
        model = SwabMasterTSR
        fields = "__all__"

    def get_part_type(self, obj):
        return "SM Tube Seal Rack"


################################################################################
#                DeviceHose Serializer
################################################################################


class DeviceHoseSerializer(serializers.ModelSerializer):
    part_type = serializers.SerializerMethodField()

    class Meta:
        model = DeviceHose
        fields = "__all__"

    def get_part_type(self, obj):
        return "Device Hose"


################################################################################
#                AirHose Serializer
################################################################################


class AirHoseSerializer(serializers.ModelSerializer):
    warehouse = serializers.StringRelatedField()
    part_type = serializers.SerializerMethodField()

    class Meta:
        model = AirHose
        fields = "__all__"

    def get_part_type(self, obj):
        return "Air Hose"


################################################################################
#                Calibration Serializer
################################################################################


class Calibration_orifice_serializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()
    part_type = serializers.SerializerMethodField()

    class Meta:
        model = Calibration_orifice
        fields = "__all__"

    def get_part_type(self, obj):
        return "Calibration orifice"


################################################################################
#                AirHose Serializer
################################################################################


class AirHoseCreSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = AirHose
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        return super().validate(data)


################################################################################
#                DeviseHose Serializer
################################################################################


class DeviceHoseListSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(
        fields=(
            "id",
            "warehouse_name",
            "warehouse_location",
        )
    )

    class Meta:
        model = DeviceHose
        fields = "__all__"


################################################################################
#                DeviseHose Serializer
################################################################################


class DeviceHoseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceHose
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        return super().validate(data)


################################################################################
#                Swabmastertsr Serializer
################################################################################


class SwabMasterTSRCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwabMasterTSR
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "serial_number")

        return super().validate(data)


################################################################################
#                CalibrationOrifice Serializer
################################################################################

from tube.serializers import WarehouseSerializer


class CalibratiobOrificeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibration_orifice
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["location_for_warehouse"] = WarehouseSerializer(
            instance.location_for_warehouse,
            fields=("id", "warehouse_name", "warehouse_location"),
        ).data
        return data

    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        return super().validate(data)


################################################################################
#                CalibrationOrificeCreate Serializer
################################################################################


class CalibratiobOrificeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibration_orifice
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        return super().validate(data)


################################################################################
#                BddTubesealrackList Serializer
################################################################################


class BddTubesealrackListSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = BDD_tube_seal_rack
        fields = "__all__"


################################################################################
#                BddTubesealrackCreate Serializer
################################################################################


class BddTubesealrackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BDD_tube_seal_rack
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        return super().validate(data)


################################################################################
#                TddTubesealrackList Serializer
################################################################################


class TddTubesealrackListSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = TTD_tube_seal_rack
        fields = "__all__"


################################################################################
#                TddTubesealrackCreate Serializer
################################################################################


class TddTubesealrackCreateSerializer(serializers.ModelSerializer):
    part_type = serializers.SerializerMethodField()

    class Meta:
        model = TTD_tube_seal_rack
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "serial_number")

        return super().validate(data)

    def get_part_type(self, obj):
        return "TTD tube seal rack"


################################################################################
#                PressuresensorList Serializer
################################################################################


class PressuresensorListSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = Pressure_sensor
        fields = "__all__"


################################################################################
#                PressuresensorCreate Serializer
################################################################################


class PressuresensorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure_sensor
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "serial_number")

        return super().validate(data)


################################################################################
#                SupplyOrificeList Serializer
################################################################################


class SupplyOrificeListSerializer(DynamicModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = Supply_orifice
        fields = "__all__"


################################################################################
#                SupplyOrificeCreate Serializer
################################################################################


class SupplyOrificeCreateSerializer(serializers.ModelSerializer):
    part_type = serializers.SerializerMethodField()

    class Meta:
        model = Supply_orifice
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        return super().validate(data)

    def get_part_type(self, obj):
        return "Supply orifice"


################################################################################
#                AllGeneralPartList Serializer
################################################################################


class AllGeneralPartListSerializer(DynamicModelSerializer):
    location_for_warehouse = WarehouseSerializer(
        fields=(
            "id",
            "warehouse_name",
            "warehouse_location",
        )
    )

    class Meta:
        model = Part
        fields = "__all__"


################################################################################
#                AllGeneralPartCreate Serializer
################################################################################


class AllGeneralPartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "part_name")
        return super().validate(data)


class WarehousePartSerializer(serializers.Serializer):
    general_part = serializers.SerializerMethodField()
    supply_orifice = serializers.SerializerMethodField()
    pressure_sensor = serializers.SerializerMethodField()
    ttd_rack = serializers.SerializerMethodField()
    bdd_rack = serializers.SerializerMethodField()
    calibration_orifice = serializers.SerializerMethodField()
    swabmasterTSR = serializers.SerializerMethodField()
    devicehose = serializers.SerializerMethodField()
    airhose = serializers.SerializerMethodField()
    # Query_params

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_query_params(self.context.get("request"))

    def get_supply_orifice(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = Supply_orifice.objects.all()
        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)
        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)

        serializer = SupplyOrificeCreateSerializer(qs, many=True)
        return serializer.data

    def get_part_data(self, qs):
        if self.pm_status != "NONE":
            qs = qs.filter(pm_status=self.pm_status)
        if self.slug:
            qs = qs.filter(location_for_warehouse__slug=self.slug)

    def get_pressure_sensor(self, obj):
        qs = Pressure_sensor.objects.all()

        serializer = SupplyOrificeCreateSerializer(qs, many=True)
        return serializer.data

    def get_ttd_rack(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = TTD_tube_seal_rack.objects.all()

        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)
        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)

        serializer = TddTubesealrackCreateSerializer(qs, many=True)
        return serializer.data

    def get_bdd_rack(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = BDD_tube_seal_rack.objects.all()

        if pm_status != "NONE":
            print(pm_status)
            qs = qs.filter(pm_status=pm_status)
        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)

        serializer = BDDTubeSealRackSerializer(qs, many=True)
        return serializer.data

    def get_calibration_orifice(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = Calibration_orifice.objects.all()
        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)
        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)

        serializer = Calibration_orifice_serializer(qs, many=True)
        return serializer.data

    def get_swabmasterTSR(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = SwabMasterTSR.objects.all()

        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)
        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)

        serializer = SwabMasterTSRSerializer(qs, many=True)
        return serializer.data

    def get_devicehose(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = DeviceHose.objects.all()

        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)
        if slug:
            qs = qs.filter(warehouse__slug=slug)

        serializer = DeviceHoseSerializer(qs, many=True)
        return serializer.data

    def get_airhose(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = AirHose.objects.all()

        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)
        if slug:
            qs = qs.filter(warehouse__slug=slug)

        serializer = AirHoseSerializer(qs, many=True)
        return serializer.data
