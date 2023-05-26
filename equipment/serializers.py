from rest_framework import serializers
from .models import *
from tube.models import *
from part.models import *
from rest_framework import serializers
from django_countries import countries

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


	

	
class TTDSerializers(serializers.ModelSerializer):
	location_for_warehouse = serializers.StringRelatedField()
	supply_orifice_set = serializers.StringRelatedField()
	pressure_sensor = serializers.StringRelatedField()
	TTD_tube_seal_rack = serializers.StringRelatedField()
	# pressure_sensor =
	# TTD_tube_seal_rack =
	class Meta:
		model = TTD
		# fields = "__all__"
		fields = ("id","abbreviation", "alternate_name", "serial_number", "asset_number", "remarks", "location_for_warehouse","pm_status", "location_for_storage", 
				  "packaging", "if_yes_how_many_in_a_set", "supply_orifice_set", "pressure_sensor", "TTD_tube_seal_rack", "frame", "image")
		# depth = 1

class TTDWithIDSerializer(serializers.ModelSerializer):
	class Meta:
		model = TTD
		fields = "__all__"
##################################################################
#       BDD Serializer
##################################################################

class BDDSerializer(serializers.ModelSerializer):
	BDD_tube_seal_rack = serializers.StringRelatedField()
	location_for_warehouse = serializers.StringRelatedField()
	class Meta:
		model = BDD
		fields = "__all__"
		
##################################################################
#       CALIBRATION_STAND Serializer
##################################################################

class CalibrationStandSerializer(serializers.ModelSerializer):
	class Meta:
		model = CALIBRATION_STAND
		fields = "__all__"

##################################################################
#       SwabMaster Serializer
##################################################################

class SwabMasterSerializer(serializers.ModelSerializer):
	class Meta:
		model = SwabMaster
		fields = "__all__"


##################################################################
#       Warehouse Serializer
##################################################################






class WarehouseSerializer(serializers.ModelSerializer):
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
		
