from django.contrib import admin
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
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

        export_as_csv.short_description = "Export Selected"
     


class PartAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_filter=['part_name']
    list_display = ('part_name', 'name_of_abbreviation', 'serial_number', 'asset_number', 'pm_status'
    , 'location_for_storage','location_for_warehouse', 'packaging','notes','upload_file','weight','price',)
    search_fields = ['part_name']
   
    actions = ["export_as_csv"]
    # radio_fields={'pm_status':admin.HORIZONTAL} 
    
    radio_fields={
        'pm_status':admin.HORIZONTAL,
        "dimension_unit": admin.HORIZONTAL,
        "weight_unit": admin.HORIZONTAL,
        } 
    
    fieldsets = (
        ('General Info', {
            "fields": (
            'part_name',
            'name_of_abbreviation',
            'serial_number',
            'asset_number',
            'pm_status',
            'location_for_warehouse',
            'location_for_storage',
            'packaging',
            'notes',
            'upload_file',
            'price',
            ),
        }),
        ('weight', {
            'fields': (
                'weight_unit',
                'weight',
            )
        }),
        ('Dimensions', {
            'fields': (
                'dimension_unit',
                'length',
                'breadth',
                'height',
            )
        }),
    )
    
admin.site.register(Part,PartAdmin)

@admin.register(Supply_orifice)
class Supply_orificeAdmin(admin.ModelAdmin):
    radio_fields={
        "dimension_unit": admin.HORIZONTAL,
        "weight_unit": admin.HORIZONTAL,
        } 

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
                'part_name',
                'name_of_abbreviation',
                'serial_number',
                'asset_number',
                'pm_status',
                'location_for_warehouse',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'price',
            ),
        }),
        ("Specific Info", {
            "fields": (
                'size',
                'total_sets',
                'orifice_in_each_set',
                'storage_case',
            )
        }),
        ("Dimensions", {
            "fields": (
                'dimension_unit',
                'length',
                'breadth',
                'height',
            )
        }),
        ("Weight", {
            "fields":(
                "weight_unit",
                "weight",
            )
        }),
    )
    
    
@admin.register(BDD_tube_seal_rack)
class BDD_tube_seal_rackAdmin(admin.ModelAdmin):
    radio_fields={
        "dimension_unit": admin.HORIZONTAL,
        "weight_unit": admin.HORIZONTAL,
        } 
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
                'part_name',
                'name_of_abbreviation',
                'serial_number',
                'asset_number',
                'pm_status',
                'location_for_warehouse',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'price',
            ),
        }),
        ("Specific Info", {
            "fields": (
                'size',
                'number_of_tubes',
            )
        }),
        ("Dimensions", {
            "fields": (
                'dimension_unit',
                'length',
                'breadth',
                'height',
            )
        }),
        ("Weight", {
            "fields":(
                "weight_unit",
                "weight",
            )
        }),
    )
    
  

@admin.register(Pressure_sensor)
class Pressure_sensorAdmin(admin.ModelAdmin):
    radio_fields={
        "dimension_unit": admin.HORIZONTAL,
        "weight_unit": admin.HORIZONTAL,
        } 
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
                'part_name',
                'name_of_abbreviation',
                'serial_number',
                'asset_number',
                'pm_status',
                'location_for_warehouse',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'price',
            ),
        }),
        ("Specific Info", {
            "fields": (
                'range',
                'quantity',
            )
        }),
        ("Dimensions", {
            "fields": (
                'dimension_unit',
                'length',
                'breadth',
                'height',
            )
        }),
        ("Weight", {
            "fields":(
                "weight_unit",
                "weight",
            )
        }),
    )
    
  
@admin.register(TTD_tube_seal_rack)
class TTD_tube_seal_rackAdmin(admin.ModelAdmin):
    radio_fields={
        "dimension_unit": admin.HORIZONTAL,
        "weight_unit": admin.HORIZONTAL,
        } 
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
                'part_name',
                'name_of_abbreviation',
                'serial_number',
                'asset_number',
                'pm_status',
                'location_for_warehouse',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'price',
            ),
        }),
        ("Specific Info", {
            "fields": (
                'size',
                'qty_rack',
                'tube_seal_rack',
                
            )
        }),
        ("Dimensions", {
            "fields": (
                'dimension_unit',
                'length',
                'breadth',
                'height',
            )
        }),
        ("Weight", {
            "fields":(
                "weight_unit",
                "weight",
            )
        }),
    )
    
  
  

@admin.register(Calibration_orifice)
class Calibration_orificeAdmin(admin.ModelAdmin):
    radio_fields={
        "dimension_unit": admin.HORIZONTAL,
        "weight_unit": admin.HORIZONTAL,
        } 
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
                'part_name',
                'name_of_abbreviation',
                'serial_number',
                'asset_number',
                'pm_status',
                'location_for_warehouse',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'price',
            ),
        }),
        ("Specific Info", {
            "fields": (
                'size',
                'total_sets',
                'in_sets',
                
            )
        }),
        ("Dimensions", {
            "fields": (
                'dimension_unit',
                'length',
                'breadth',
                'height',
            )
        }),
        ("Weight", {
            "fields":(
                "weight_unit",
                "weight",
            )
        }),
    )
    
  

from .models import *

@admin.register(SwabMasterTSR)
class SwabMaster_TSRadmin(admin.ModelAdmin):
    radio_fields={
        "dimension_unit": admin.HORIZONTAL,
        "weight_unit": admin.HORIZONTAL,
        } 
    list_display = ['serial_number','size','qty_rack','tube_seal_rack','location_for_warehouse']
    search_fields=['serial_number']
    list_filter = ['serial_number', 'size']
   

    fieldsets = (
        ("General", {
            "fields": (
                'part_name',
                'name_of_abbreviation',
                'serial_number',
                'asset_number',
                'pm_status',
                'location_for_warehouse',
                'location_for_storage',                
                'packaging',
                'notes',
                'upload_file',
                'price',
            ),
        }),
        ("Specific Info", {
            "fields": (
                'size',
                'qty_rack',
                'tube_seal_rack',
                
            )
        }),
        ("Dimensions", {
            "fields": (
                'dimension_unit',
                'length',
                'breadth',
                'height',
            )
        }),
        ("Weight", {
            "fields":(
                "weight_unit",
                "weight",
            )
        }),
    )
    
  
  
@admin.register(DeviceHose)
class DeviceHoseAdmin(admin.ModelAdmin):
    radio_fields={
        "dimension_unit": admin.HORIZONTAL,
        "weight_unit": admin.HORIZONTAL,
        } 
    # list_filter= ['serial_number','colour_code','warehouse']
    # search_fields=['serial_number','colour_code','warehouse']
    # list_display= ['serial_number','length','colour_code','warehouse']

    fieldsets = (
        ("General", {
            "fields": (
                    "part_name",
                    "name_of_abbreviation",
                    "serial_number",
                    "asset_number",
                    "pm_status",
                    "warehouse",
                    "location_for_storage",
                    "packaging",
                    "notes",
                    "upload_file",
                    "price",
                
            ),
        }),
        ( "Specific Info", {
            'fields': (
                'colour_code',
                
            )
        }),
        ("Dimensions", {
            "fields": (
                'dimension_unit',
                'length',
                'breadth',
                'height',
            )
        }),
        ("Weight", {
            "fields":(
                "weight_unit",
                "weight",
            )
        }),

    )
    

@admin.register(AirHose)
class AirHosesAdmin(admin.ModelAdmin):
    radio_fields={
        "dimension_unit": admin.HORIZONTAL,
        "weight_unit": admin.HORIZONTAL,
        } 
    
    fieldsets = (
        ('General', {
            "fields": (
                "part_name",
                "name_of_abbreviation",
                "serial_number",
                "asset_number",
                "pm_status",
                "warehouse",
                "location_for_storage",
                "packaging",
                "notes",
                "upload_file",
                "price",
                
            ),
        }),
        (
            "Specific Info",
            {
                "fields": (
                    "colour_code",
                ),
            },
        ),
        ("Dimensions", {
            "fields": (
                'dimension_unit',
                'length',
                'breadth',
                'height',
            )
        }),
            ("Weight", {
            "fields":(
                "weight_unit",
                "weight",
            )
        }),
    )
    

    list_filter = ["serial_number", "colour_code", "warehouse"]
    search_fields = [
        "serial_number",
        "colour_code",
        "warehouse",
    ]
    list_display = ["serial_number", "length", "colour_code", "warehouse"]

