from rest_framework import serializers
from .models import *
from project.validators import SerialValidator

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

    class Meta:
        model = Pressure_sensor
        fields = "__all__"


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

    class Meta:
        model = BDD_tube_seal_rack
        fields = "__all__"


################################################################################
#                SwabMaster Serializer
################################################################################


class SwabMasterTSRSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = SwabMasterTSR
        fields = "__all__"


################################################################################
#                DeviceHose Serializer
################################################################################


class DeviceHoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceHose
        fields = "__all__"


################################################################################
#                AirHose Serializer
################################################################################


class AirHoseSerializer(serializers.ModelSerializer):
    warehouse = serializers.StringRelatedField()

    class Meta:
        model = AirHose
        fields = "__all__"


################################################################################
#                Calibration Serializer
################################################################################


class Calibration_orifice_serializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = Calibration_orifice
        fields = "__all__"


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
    warehouse = serializers.StringRelatedField()

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


class CalibratiobOrificeSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = Calibration_orifice
        fields = "__all__"

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
    class Meta:
        model = TTD_tube_seal_rack
        fields = "__all__"


    def validate(self, data):
        SerialValidator(self, data, "serial_number")

        return super().validate(data)

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


class SupplyOrificeListSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

    class Meta:
        model = Supply_orifice
        fields = "__all__"


################################################################################
#                SupplyOrificeCreate Serializer
################################################################################


class SupplyOrificeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply_orifice
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "serial_number")
        return super().validate(data)
################################################################################
#                AllGeneralPartList Serializer
################################################################################


class AllGeneralPartListSerializer(serializers.ModelSerializer):
    location_for_warehouse = serializers.StringRelatedField()

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

    def get_general_part(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = Part.objects.all()

        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)

        if slug:
            print("slug is not none")
            qs = qs.filter(location_for_warehouse__slug=slug)

        serializer = AllGeneralPartCreateSerializer(qs, many=True)
        return serializer.data

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

    def get_pressure_sensor(self, obj):
        request = self.context.get("request")
        slug = request.query_params.get("slug")
        pm_status = str(request.query_params.get("pm_status")).upper()
        qs = Pressure_sensor.objects.all()
        if pm_status != "NONE":
            qs = qs.filter(pm_status=pm_status)
        if slug:
            qs = qs.filter(location_for_warehouse__slug=slug)

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
    
