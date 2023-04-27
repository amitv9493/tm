from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from part.models import Part
from part.models import Supply_orifice
from part.models import Pressure_sensor
from part.models import TTD_tube_seal_rack
from part.models import BDD_tube_seal_rack
from part.models import Calibration_orifice
import csv
from django.http import HttpResponse


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

        export_as_csv.short_description = "Export Selected"
     


class PartAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_filter=['part_name']
    list_display = ('part_name', 'name_of_abbreviation', 'serial_number', 'asset_number', 'pm_status'
    , 'location_for_storage', 'packaging','notes','upload_file','weight','price','dimension',)
    search_fields = ['part_name']
   
    actions = ["export_as_csv"]
    # radio_fields={'pm_status':admin.HORIZONTAL} 
    
admin.site.register(Part,PartAdmin)

@admin.register(Supply_orifice)
class Supply_orificeAdmin(admin.ModelAdmin):

    def Is_used(self, obj):
            try:
                if obj.TTD:
                    return 'Yes'
            except:
                return 'No'

    list_filter=['size',]
    list_display = ['serial_number', 'size', 'total_sets','storage_case','Is_used','location_for_warehouse']
    search_fields = ['serial_number', 'size', 'total_sets','storage_case',]

    fieldsets = (
        ("General", {
            "fields": (
                'serial_number',
                'location_for_warehouse',
                'part_name',
                'name_of_abbreviation',
                'asset_number',
                'pm_status',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'weight',
                'price',
                'dimension', 
            ),
        }),
        ("Specific Info", {
            "fields": (
                'size',
                'total_sets',
                'orifice_in_each_set',
                'storage_case',
            )
        })
    )
    
    
@admin.register(BDD_tube_seal_rack)
class BDD_tube_seal_rackAdmin(admin.ModelAdmin):

    def Is_used(self, obj):
            try:
                if obj.bdd:
                    return 'Yes'
            except:
                return 'No'

    list_filter=['size',]
    list_display = ['serial_number','size','number_of_tubes','Is_used','location_for_warehouse']
    search_fields = ['serial_number','size','tube_seal_rack']

    fieldsets = (
        ("General", {
            "fields": (
                'serial_number',
                'location_for_warehouse',
                'part_name',
                'name_of_abbreviation',
                'asset_number',
                'pm_status',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'weight',
                'price',
                'dimension', 
            ),
        }),
        ("Specific Info", {
            "fields": (
                'size',
                'number_of_tubes',
            )
        })
    )
    
  

@admin.register(Pressure_sensor)
class Pressure_sensorAdmin(admin.ModelAdmin):

    def Is_used(self, obj):
            try:
                if obj.TTD:
                    return 'Yes'
            except:
                return 'No'


    list_filter=['range',]

    list_display = ['serial_number','range','Is_used','location_for_warehouse',]

    search_fields = ['serial_number',
                'range',]
# class Pressure_sensorAdmin(admin.ModelAdmin):

    # def has_module_permission(self, request):
    #     return False 
    

    fieldsets = (
        ("General", {
            "fields": (
                'serial_number',
                'location_for_warehouse',
                'part_name',
                'name_of_abbreviation',
                'asset_number',
                'pm_status',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'weight',
                'price',
                'dimension', 
            ),
        }),
        ("Specific Info", {
            "fields": (
                'range',
                'quantity',
            )
        })
    )
    
  
@admin.register(TTD_tube_seal_rack)
class TTD_tube_seal_rackAdmin(admin.ModelAdmin):

    def Is_used(self, obj):
            try:
                if obj.TTD:
                    return 'Yes'
            except:
                return 'No'


    list_filter=['size',]
    list_display = ['serial_number',
                    'size',
                    'Is_used',
                    'location_for_warehouse',

                    ]
    search_fields = ['serial_number',
                    'size',
                    ]  

   

    fieldsets = (
        ("General", {
            "fields": (
                'serial_number',
                'location_for_warehouse',
                'part_name',
                'name_of_abbreviation',
                'asset_number',
                'pm_status',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'weight',
                'price',
                'dimension', 
            ),
        }),
        ("Specific Info", {
            "fields": (
                'size',
                'qty_rack',
                'tube_seal_rack',
                
            )
        })
    )
    
  
  

@admin.register(Calibration_orifice)
class Calibration_orificeAdmin(admin.ModelAdmin):

    def Is_used(self,obj):
         try:
            if obj.TTD:
                return "Yes"
              
         except:
              return 'No'

    list_filter=['size',]
    
    search_fields = ['serial_number',
                     'size',
                     
                     ]
    
    list_display = ['serial_number',
                    'size',
                    'Is_used',
                    'location_for_warehouse',
                    
                    ]

# class TTD_tube_seal_rackAdmin(admin.ModelAdmin):

    # def has_module_permission(self, request):
    #     return False 

# class BDD_tube_seal_rackAdmin(admin.ModelAdmin):

    # def has_module_permission(self, request):
    #     return False 

# class Calibration_orificeAdmin(admin.ModelAdmin):

    # def has_module_permission(self, request):
    #     return False 

   

    fieldsets = (
        ("General", {
            "fields": (
                'serial_number',
                'location_for_warehouse',
                'part_name',
                'name_of_abbreviation',
                'asset_number',
                'pm_status',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'weight',
                'price',
                'dimension', 
            ),
        }),
        ("Specific Info", {
            "fields": (
                'size',
                'total_sets',
                'in_sets',
                
            )
        })
    )
    
  

from .models import *

@admin.register(SwabMasterTSR)
class SwabMaster_TSRadmin(admin.ModelAdmin):
    list_display = ['serial_number','size','qty_rack','tube_seal_rack','location_for_warehouse']
    search_fields=['serial_number']
    list_filter = ['serial_number', 'size']
   

    fieldsets = (
        ("General", {
            "fields": (
                'serial_number',
                'location_for_warehouse',
                'part_name',
                'name_of_abbreviation',
                'asset_number',
                'pm_status',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'weight',
                'price',
                'dimension', 
            ),
        }),
        ("Specific Info", {
            "fields": (
                'size',
                'qty_rack',
                'tube_seal_rack',
                
            )
        })
    )
    
  
  
@admin.register(DeviceHose)
class DeviceHoseAdmin(admin.ModelAdmin):
    # list_filter= ['serial_number','colour_code','warehouse']
    # search_fields=['serial_number','colour_code','warehouse']
    # list_display= ['serial_number','length','colour_code','warehouse']

    fieldsets = (
        ("General", {
            "fields": (
                    "warehouse",
                    "serial_number",
                    "part_name",
                    "name_of_abbreviation",
                    "asset_number",
                    "pm_status",
                    "location_for_storage",
                    "packaging",
                    "notes",
                    "upload_file",
                    "weight",
                    "price",
                    "dimension",
                
            ),
        }),
        ( "Specific Info", {
            'fields': (
                'length',
                'colour_code',
                
            )
        }),

    )
    

@admin.register(AirHose)
class AirHosesAdmin(admin.ModelAdmin):
    fieldsets = (
        
        (
            "General",
            {
                "fields": (
                    "warehouse",
                    "serial_number",
                    "part_name",
                    "name_of_abbreviation",
                    "asset_number",
                    "pm_status",
                    "location_for_storage",
                    "packaging",
                    "notes",
                    "upload_file",
                    "weight",
                    "price",
                    "dimension",
                ),
            },
        ),
        (
            "Specific Info",
            {
                "fields": (
                    "length",
                    "colour_code",
                ),
            },
        ),
    )

    list_filter = ["serial_number", "colour_code", "warehouse"]
    search_fields = [
        "serial_number",
        "colour_code",
        "warehouse",
    ]
    list_display = ["serial_number", "length", "colour_code", "warehouse"]

