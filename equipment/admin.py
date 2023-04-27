from django.contrib import admin

# Register your models here.


# Register your models here.

from equipment.models import TTD, SwabMaster
from equipment.models import BDD
from equipment.models import CALIBRATION_STAND
from import_export.admin import ImportExportModelAdmin
from .forms import *

class TTDAdmin(ImportExportModelAdmin):
    form = TTDForm
    list_filter= ['serial_number','location_for_storage','location_for_warehouse','pm_status']

    list_display = ('abbreviation','serial_number','asset_number','location_for_warehouse','location_for_storage','supply_orifice_set','pressure_sensor','TTD_tube_seal_rack','pm_status')
    fieldsets = [
        ('Warehouse Info', {
           
            'fields': ['location_for_warehouse', 'location_for_storage','packaging', 'is_this_part_of_set','if_yes_how_many_in_a_set'],
        }),
        ('TTD Info', {
            'fields': [ 'abbreviation','alternate_name','serial_number','asset_number','pm_status','frame','image','remarks'],
        }),
       
        ('Specification', {
           
            'fields': ['supply_orifice_set', 'pressure_sensor','TTD_tube_seal_rack'],
        }),
   
        ]
    radio_fields = {'pm_status': admin.HORIZONTAL,'is_this_part_of_set':admin.HORIZONTAL}
    
     
    search_fields = [
                    'serial_number',
                    'abbreviation',
                    'asset_number',
                    'location_for_warehouse__warehouse_name',
                    'location_for_storage',
                    'supply_orifice_set__size',
                    ]
    # def list_of_supply_orifice_set(self, obj):
    #     return ("%s" % ','.join([supply_orifice_set.size for supply_orifice_set in obj.supply_orifice_set.all()]))
    # list_of_supply_orifice_set.short_description = 'Supply Orifice Set'
    
    # def has_module_permission(self, request):
    #     return False    
admin.site.register(TTD,TTDAdmin)

class BDDAdmin(ImportExportModelAdmin):
    form = BDDForm
    list_filter= ['serial_number','location_for_storage','location_for_warehouse']

    list_display = ('abbreviation','serial_number','asset_number','location_for_warehouse','location_for_storage','BDD_tube_seal_rack')
    fieldsets = [
        ('Warehouse Info', {
           
            'fields': ['location_for_warehouse', 'location_for_storage','packaging', 'is_this_part_of_set','if_yes_how_many_in_a_set'],
        }),
        ('BDD Info', {
            'fields': [ 'abbreviation','alternate_name','serial_number','asset_number','pm_status','remarks'],
        }),
        
        ('Specification', {
           
            'fields': ['BDD_tube_seal_rack', 'frame','image'],
        }),
   
        ]
    radio_fields = {'pm_status': admin.HORIZONTAL,'is_this_part_of_set':admin.HORIZONTAL}
    search_fields = [
                    'serial_number',
                     'abbreviation',
                     'asset_number',
                     'location_for_warehouse__warehouse_name',
                     'BDD_tube_seal_rack__size',
                     'location_for_storage',
                     ]

    # def list_of_parts(self, obj):
    #     return ("%s" % ','.join([allow_to_add_sub_parts.part_name for allow_to_add_sub_parts in obj.allow_to_add_sub_parts.all()]))
    # list_of_parts.short_description = 'Parts'

    # def has_module_permission(self, request):
    #     return False   

admin.site.register(BDD,BDDAdmin)

class CALIBRATION_STANDAdmin(ImportExportModelAdmin):
    form = CALIBRATION_STANDForm

    list_filter= ['serial_number','location_for_storage','location_for_warehouse']

    list_display = ('abbreviation','serial_number','asset_number','location_for_warehouse','location_for_storage','cal_stand_size','calibration_orifice_set')
    fieldsets = [
        ('Warehouse Info', {
           
            'fields': ['location_for_warehouse', 'location_for_storage','packaging', 'is_this_part_of_set','if_yes_how_many_in_a_set'],
        }),
        ('Calibration Stand Info', {
            'fields': [ 'abbreviation','alternate_name','serial_number','asset_number','pm_status','remarks'],
        }),
       
        ('Specification', {
           
            'fields': ['cal_stand_size','calibration_orifice_set','frame','image'],
        }),
   
        ]
    radio_fields = {'pm_status': admin.HORIZONTAL,}
    # autocomplete_fields=['is_this_part_of_set']
    
    search_fields = ('abbreviation','serial_number','asset_number','location_for_warehouse__warehouse_name','location_for_storage','cal_stand_size','calibration_orifice_set__size')

    # def list_of_parts(self, obj):
    #     return ("%s" % ','.join([allow_to_add_sub_parts.part_name for allow_to_add_sub_parts in obj.allow_to_add_sub_parts.all()]))
    # list_of_parts.short_description = 'Parts'

    # def has_module_permission(self, request):
    #     return False  
admin.site.register(CALIBRATION_STAND,CALIBRATION_STANDAdmin)

# @admin.register(SwabMaster)

class SwabMasterAdmin(admin.ModelAdmin):
    
    form = SwabMasterForm
    list_display = ['abbreviation', 'serial_number','asset_number','location_for_warehouse', 'location_for_storage', 'Swab_Master_Tube_Seal_Rack']

    fieldsets = [
        ('Warehouse Info', {
           
            'fields': ['location_for_warehouse', 'location_for_storage','packaging', 'is_this_part_of_set','if_yes_how_many_in_a_set'],
        }),
        ('Swab Master Info', {
            'fields': [ 'abbreviation','alternate_name','serial_number','asset_number','pm_status','remarks'],
        }),
       
        ('Specification', {
           
            'fields': ['Swab_Master_Tube_Seal_Rack', 'Generation_1','Generation_2'],
        }),
   
        ]

admin.site.register(SwabMaster, SwabMasterAdmin)
