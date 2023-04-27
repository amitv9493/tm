
from rest_framework import serializers
from django.contrib.auth.models import User
from client.models import *
from part.models import *
from equipment.models import *
from tube.models import *
from django_countries.serializers import CountryFieldMixin

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
        model=User
        fields = [ 'username' ,'password']

    

################################################################################
#            Client API Serializer
################################################################################


class ClientSerializer(CountryFieldMixin,serializers.ModelSerializer):
    
   class Meta:
      model = Client
      fields =['id', 'official_name', 'country']


################################################################################
#            Unit API Serializer
################################################################################


class UnitSerializer(serializers.ModelSerializer):
       class Meta:
        model = Unit
        fields = ('id','name_of_unit')
        
################################################################################
#            SOW API Serializer
################################################################################
from project.models import *

class SOWSerializer(serializers.ModelSerializer):
       class Meta:
        model = Scope_of_work
        fields = ('id','name')

################################################################################
#            TTD API Serializer
################################################################################
class WarehouseLocationSerializer(CountryFieldMixin,serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id','warehouse_location','country',]

class TtdSerializer(serializers.ModelSerializer):
    location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = TTD 
        # fields = ('id', 'serial_number')
        fields = ['id', 'serial_number', 'location_for_warehouse', 'pm_status','alternate_name']
        # depth = 1
        
################################################################################
#            BDD API Serializer
################################################################################
        
class BddSerializer(serializers.ModelSerializer):
    location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = BDD
        # fields = "__all__"
        fields = ['id', 'serial_number', 'location_for_warehouse', 'pm_status','alternate_name']
        
################################################################################
#            Calibration API Serializer
################################################################################
        
class CALIBRATION_STANDSerializer(serializers.ModelSerializer):
    location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = CALIBRATION_STAND
        # fields = "__all__"
        fields = ['id', 'serial_number', 'location_for_warehouse', 'pm_status','alternate_name'] 
        
################################################################################
#            Part API Serializer
################################################################################

class PartSerializer(serializers.ModelSerializer):
    location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = Part
        # fields = "__all__"
        fields = ['id', 'part_name' ,'serial_number', 'location_for_warehouse', 'pm_status']
        
################################################################################
#            Supply API Serializer
################################################################################
        
class SupplyOrificeSerializer(serializers.ModelSerializer):
    location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = Supply_orifice
        # fields = "__all__"
        fields = ['id','serial_number', 'size', 'total_sets','orifice_in_each_set','storage_case','location_for_warehouse']         
        
        
        
        
        
################################################################################
#                            reactor 
################################################################################
class ReactorSerializer(serializers.ModelSerializer):
    # location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = Reactor
        # fields = "_all_"
        fields = ['id', 'reactor_name']
        

################################################################################
#                       pressuresensor 
################################################################################        
class PressureSensorSerializer(serializers.ModelSerializer):
    location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = Pressure_sensor
        fields = ('id','serial_number','quantity','range','location_for_warehouse')
        
        
################################################################################
#            calibration 
################################################################################
class CalibrationOrificeSerializer(serializers.ModelSerializer):
    location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = Calibration_orifice
        fields = ('id','serial_number','size','total_sets','in_sets','location_for_warehouse')       
        
        
################################################################################
#            swabmaster 
################################################################################
class SwabMasterSerializer(serializers.ModelSerializer):
    location_for_warehouse = WarehouseLocationSerializer()
    class Meta:
        model = SwabMasterTSR
        fields = ('id','serial_number','size','qty_rack','tube_seal_rack','location_for_warehouse')
        
################################################################################
#            deviceair 
################################################################################
class DeviceHoseSerializer(serializers.ModelSerializer):
    warehouse = WarehouseLocationSerializer()
    class Meta:
        model = DeviceHose
        fields = ('id','serial_number','length','colour_code','warehouse')

################################################################################
#            airhose
################################################################################
class AirHoseSerializer(serializers.ModelSerializer):
    warehouse = WarehouseLocationSerializer()
    class Meta:
        model = AirHose
        fields = ('id','serial_number','length','colour_code','warehouse')
        
################################################################################
#            AllListWithId Serializer
################################################################################
# from django.forms.models import model_to_dict


class Add_Project_serializer(serializers.ModelSerializer):
    client = ClientSerializer()
    class Meta:
        model = Project
        # fields = ('id','project_name','project_number','equipment_prep','client','ttd','unit','scope_of_work','bdd','calibration_stand','part','supply_orifice_part','reactor','pressure_sensor_part','calibration_orifice_part','swabmaster_part','device_part','airhose_part')
        fields ="__all__"
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


################################################################################
#            GET_Project_serializer Serializer
################################################################################
# from django.forms.models import model_to_dict

class GET_Project_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        # fields = ('id','project_name','project_number','equipment_prep','client','ttd','unit','scope_of_work','bdd','calibration_stand','part','supply_orifice_part','reactor','pressure_sensor_part','calibration_orifice_part','swabmaster_part','device_part','airhose_part')
        fields ="__all__"
        # depth = 1
    
    
################################################################################
#            List Serializer
################################################################################

class AllList_Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields ="__all__"
        # depth = 1
    
################################################################################
#            Create Serializer
################################################################################

class Create_Project_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields ="__all__"
        # fields = ""
        
################################################################################
#            Project Patch Serializer
################################################################################

class All_Project_Patch_serializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields ="__all__"       
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        