from rest_framework import serializers
from django.contrib.auth.models import User
from client.models import *
from part.models import *
from equipment.models import *
from tube.models import *
from django_countries.serializers import CountryFieldMixin
from project.validators import SerialValidator
from core.serializers import DynamicModelSerializer
from part.serializers import (
    AllGeneralPartListSerializer,
    PressuresensorListSerializer,
    CalibratiobOrificeSerializer,
    SupplyOrificeListSerializer,
    SwabMasterTSRSerializer,
    DeviceHoseListSerializer,
    AirHoseSerializer,
)


################################################################################
#            Login API Serializer
################################################################################


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email"]


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["username", "password"]


################################################################################
#            Client API Serializer
################################################################################


class ClientSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Client
        # fields = ["id", "official_name", "country"]
        # fields = "_all_"
        fields = ["official_name"]
        read_only_fields = ["official_name"]

    def to_representation(self, instance):
        return instance.official_name


################################################################################
#            Unit API Serializer
################################################################################


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ["name_of_unit"]
        read_only_fields = ["name_of_unit"]

    def to_representation(self, instance):
        return instance.name_of_unit


################################################################################
#            SOW API Serializer
################################################################################
from project.models import *


class SOWSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope_of_work
        fields = ("id", "name")


################################################################################
#            TTD API Serializer
################################################################################
class WarehouseLocationSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            "id",
            "warehouse_location",
            "country",
        ]


class TtdSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view_name = self.context.get("view").__class__.__name__
        # print((self.fields["location_for_warehouse"].Meta.fields))

        if view_name == "TTDNewView":
            print("new endpoint")
            (self.fields["location_for_warehouse"].Meta.fields) = "__all__"
        else:
            (self.fields["location_for_warehouse"].Meta.fields) = [
                "id",
                "warehouse_location",
                "country",
            ]

    location_for_warehouse = WarehouseLocationSerializer()

    class Meta:
        model = TTD
        # fields = ('id', 'serial_number')
        fields = [
            "id",
            "serial_number",
            "location_for_warehouse",
            "pm_status",
            "alternate_name",
        ]
        # depth = 1


################################################################################
#            BDD API Serializer
################################################################################


class BddSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view_name = self.context.get("view").__class__.__name__
        print(view_name)
        print((self.fields["location_for_warehouse"].Meta.fields))

        if view_name == "BddNewView":
            (self.fields["location_for_warehouse"].Meta.fields) = "__all__"
        else:
            (self.fields["location_for_warehouse"].Meta.fields) = [
                "id",
                "warehouse_location",
                "country",
            ]

    location_for_warehouse = WarehouseLocationSerializer()

    class Meta:
        model = BDD
        # fields = "__all__"
        fields = [
            "id",
            "serial_number",
            "location_for_warehouse",
            "pm_status",
            "alternate_name",
        ]


################################################################################
#            Calibration API Serializer
################################################################################


class CALIBRATION_STANDSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view_name = self.context.get("view").__class__.__name__
        print(view_name)
        print((self.fields["location_for_warehouse"].Meta.fields))

        if view_name == "CalibrationStandNewView":
            (self.fields["location_for_warehouse"].Meta.fields) = "__all__"
        else:
            (self.fields["location_for_warehouse"].Meta.fields) = [
                "id",
                "warehouse_location",
                "country",
            ]

    location_for_warehouse = WarehouseLocationSerializer()

    class Meta:
        model = CALIBRATION_STAND
        # fields = "__all__"
        fields = [
            "id",
            "serial_number",
            "location_for_warehouse",
            "pm_status",
            "alternate_name",
        ]


################################################################################
#            Part API Serializer
################################################################################


class PartSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view_name = self.context.get("view").__class__.__name__
        print(view_name)
        print((self.fields["location_for_warehouse"].Meta.fields))

        if view_name == "PartNewView":
            (self.fields["location_for_warehouse"].Meta.fields) = "__all__"

        else:
            (self.fields["location_for_warehouse"].Meta.fields) = [
                "id",
                "warehouse_location",
                "country",
            ]

    location_for_warehouse = WarehouseLocationSerializer()

    class Meta:
        model = Part
        # fields = "__all__"
        fields = [
            "id",
            "part_name",
            "serial_number",
            "location_for_warehouse",
            "pm_status",
        ]


################################################################################
#            Supply API Serializer
################################################################################


class SupplyOrificeSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view_name = self.context.get("view").__class__.__name__
        print(view_name)
        print((self.fields["location_for_warehouse"].Meta.fields))

        if view_name == "SupplyOrificeNewView":
            (self.fields["location_for_warehouse"].Meta.fields) = "__all__"
        else:
            (self.fields["location_for_warehouse"].Meta.fields) = [
                "id",
                "warehouse_location",
                "country",
            ]

    location_for_warehouse = WarehouseLocationSerializer()

    class Meta:
        model = Supply_orifice
        # fields = "__all__"
        fields = [
            "id",
            "serial_number",
            "size",
            "total_sets",
            "orifice_in_each_set",
            "storage_case",
            "location_for_warehouse",
        ]


################################################################################
#                            reactor
################################################################################
class ReactorSerializer(serializers.ModelSerializer):
    # location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = Reactor
        # fields = "_all_"
        fields = ["id", "reactor_name"]


################################################################################
#                       pressuresensor
################################################################################
class PressureSensorSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view_name = self.context.get("view").__class__.__name__
        print(view_name)
        print((self.fields["location_for_warehouse"].Meta.fields))

        if view_name == "PressureSensorNewView":
            (self.fields["location_for_warehouse"].Meta.fields) = "__all__"
        else:
            (self.fields["location_for_warehouse"].Meta.fields) = [
                "id",
                "warehouse_location",
                "country",
            ]

    location_for_warehouse = WarehouseLocationSerializer()

    class Meta:
        model = Pressure_sensor
        fields = ("id", "serial_number", "quantity", "range", "location_for_warehouse")


################################################################################
#            calibration
################################################################################
class CalibrationOrificeSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view_name = self.context.get("view").__class__.__name__
        print(view_name)
        print((self.fields["location_for_warehouse"].Meta.fields))

        if view_name == "CalibrationOrificeNewView":
            (self.fields["location_for_warehouse"].Meta.fields) = "__all__"
        else:
            (self.fields["location_for_warehouse"].Meta.fields) = [
                "id",
                "warehouse_location",
                "country",
            ]

    location_for_warehouse = WarehouseLocationSerializer()

    class Meta:
        model = Calibration_orifice
        fields = [
            "id",
            "serial_number",
            "size",
            "total_sets",
            "in_sets",
            "location_for_warehouse",
        ]


################################################################################
#            swabmaster
################################################################################
class SwabMasterSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view_name = self.context.get("view").__class__.__name__
        print(view_name)
        print((self.fields["location_for_warehouse"].Meta.fields))

        if view_name == "SwabMasterNewView":
            (self.fields["location_for_warehouse"].Meta.fields) = "__all__"
        else:
            (self.fields["location_for_warehouse"].Meta.fields) = [
                "id",
                "warehouse_location",
                "country",
            ]

    location_for_warehouse = WarehouseLocationSerializer()

    class Meta:
        model = SwabMasterTSR
        fields = [
            "id",
            "serial_number",
            "size",
            "qty_rack",
            "tube_seal_rack",
            "location_for_warehouse",
        ]


################################################################################
#            deviceair
################################################################################
class DeviceHoseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view_name = self.context.get("view").__class__.__name__
        print(view_name)

        if view_name == "DeviceHoseNewView":
            (self.fields["warehouse"].Meta.fields) = "__all__"
        else:
            (self.fields["warehouse"].Meta.fields) = [
                "id",
                "warehouse_location",
                "country",
            ]

    warehouse = WarehouseLocationSerializer()

    class Meta:
        model = DeviceHose
        fields = ("id", "serial_number", "length", "colour_code", "warehouse")


################################################################################
#            airhose
################################################################################
class AirHoseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view_name = self.context.get("view").__class__.__name__

        if view_name == "AirHoseNewView":
            (self.fields["warehouse"].Meta.fields) = "__all__"
        else:
            (self.fields["warehouse"].Meta.fields) = [
                "id",
                "warehouse_location",
                "country",
            ]

    warehouse = WarehouseLocationSerializer()

    class Meta:
        model = AirHose
        fields = ("id", "serial_number", "length", "colour_code", "warehouse")


################################################################################
#            AllListWithId Serializer
################################################################################
# from django.forms.models import model_to_dict


class Add_Project_serializer(serializers.ModelSerializer):
    client = ClientSerializer()
    unit = UnitSerializer()

    class Meta:
        model = Project
        # fields = (
        #     "id",
        #     "slug",
        #     "project_name",
        #     "project_number",
        #     "equipment_prep",
        #     "unit",
        #     "scope_of_work",
        #     "reactor",
        #     "project_start",
        #     "project_end",
        #     "client",
        #     "ttd",
        #     "bdd",
        #     "calibration_stand",
        #     "part",
        #     "airhose_part",
        #     "device_part",
        #     "calibration_orifice_part",
        # )
        fields = "__all__"
        # exclude

        depth = 1

    # client = ClientSerializer()
    # unit = UnitSerializer()
    # scope_of_work = SOWSerializer()
    # ttd = TtdSerializer()
    # bdd = BddSerializer()
    # calibration_stand = CALIBRATION_STANDSerializer()
    # part = PartSerializer()
    # supply_orifice_part = SupplyOrificeSerializer()
    # reactor = ReactorSerializer()
    # pressure_sensor_part = PressureSensorSerializer()
    # calibration_orifice_part = CalibrationOrificeSerializer()
    # swabmaster_part = SwabMasterSerializer()
    # device_part = DeviceHoseSerializer()
    # airhose_part = AirHoseSerializer()

    # def to_representation(self, instance):
    #     return model_to_dict(instance)

    def validate(self, data):
        SerialValidator(self, data, "project_name")
        return super().validate(data)


"""################################################################################
#            GET_Project_serializer Serializer
################################################################################"""

# `serializers to use only in below serializer not anywhere else`


class TTDSerialzerProject(serializers.ModelSerializer):
    class Meta:
        model = TTD
        fields = "__all__"


class BDDSerializerProject(serializers.ModelSerializer):
    class Meta:
        model = BDD
        fields = "__all__"


class CALIBRATION_STANDSerializerProject(serializers.ModelSerializer):
    class Meta:
        model = CALIBRATION_STAND
        fields = "__all__"


class SwabMasterTSRSerializerProject(serializers.ModelSerializer):
    class Meta:
        model = SwabMaster
        fields = "__all__"


class AirHoseSerializerProject(serializers.ModelSerializer):
    class Meta:
        model = AirHose
        fields = "__all__"


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    def validate(self, data):
        SerialValidator(self, data, "project_nmae")
        return super().validate(data)


class GET_Project_serializer(serializers.ModelSerializer):
    """equipments"""

    ttd = TTDSerialzerProject(many=True)
    bdd = BDDSerializerProject(many=True)
    calibration_stand = CALIBRATION_STANDSerializerProject(many=True)
    swabmaster_equip = SwabMasterTSRSerializerProject(many=True)

    """parts"""
    # dont change below serializers
    part = AllGeneralPartListSerializer(many=True)  # dont change
    # supply_orifice_part = SupplyOrificeListSerializer(many=True)  # dont change
    # pressure_sensor_part = PressuresensorListSerializer(many=True)
    calibration_orifice_part = CalibratiobOrificeSerializer(many=True)
    # swabmaster_part = SwabMasterTSRSerializer(many=True)
    device_part = DeviceHoseListSerializer(many=True)
    airhose_part = AirHoseSerializerProject(many=True)

    class Meta:
        model = Project
        # fields = ('id','project_name','project_number','equipment_prep','client','ttd','unit','scope_of_work','bdd','calibration_stand','part','supply_orifice_part','reactor','pressure_sensor_part','calibration_orifice_part','swabmaster_part','device_part','airhose_part')
        fields = "__all__"
        # depth = 1


################################################################################
#            List Serializer
################################################################################


class AllList_Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        # depth = 1


################################################################################
#            Create Serializer
################################################################################


class Create_Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        # fields = ""

    def validate(self, data):
        SerialValidator(
            self,
            data,
            "project_name",
        )
        return data


################################################################################
#            Project Patch Serializer
################################################################################

from equipment.serializers import (
    TTDSerializers,
    BDDSerializer,
    CalibrationStandSerializer,
    SwabMasterSerializer,
)


class DynamicReactorSerializer(DynamicModelSerializer):
    class Meta:
        model = Reactor
        fields = "__all__"


from part.serializers import AirHoseSerializer
from client.serializers import ReactorCreateSerializer


class ProjectRecordSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    unit = serializers.StringRelatedField()
    reactor = ReactorCreateSerializer(
        many=True,
    )
    ttd = TTDSerializers(
        many=True,
    )
    bdd = BDDSerializer(many=True)
    calibration_stand = CalibrationStandSerializer(many=True)
    swabmaster_equip = SwabMasterSerializer(many=True)

    part = AllGeneralPartListSerializer(many=True)

    calibration_orifice_part = SupplyOrificeListSerializer(many=True)
    device_part = DeviceHoseSerializer(many=True)
    airhose_part = AirHoseSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"
