from django.contrib import admin
import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay

# Register your models here.
from project.models import Project
from project.models import Scope_of_work, ProjectStatus
from .forms import ProjectForm
from equipment.models import TTD, BDD, CALIBRATION_STAND


class ProjectStatusAdmin(admin.ModelAdmin):
    list_display= ['id', 'status']
    def has_module_permission(self, request):
       return False

admin.site.register(ProjectStatus,ProjectStatusAdmin)

class Scope_of_workAdmin(admin.ModelAdmin):
    list_display=('name',)
    def has_module_permission(self, request):
       return False 
    
admin.site.register(Scope_of_work,Scope_of_workAdmin)

class ProjectAdmin(admin.ModelAdmin):
    
    form =ProjectForm
    date_hierarchy = "created_at"
    ordering = ("-created_at",) 
    
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        if request.method == "GET":
            queryset = response.context_data["cl"].queryset
            chart_data = self.chart_data(queryset)
            as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
            response.context_data.update({"chart_data": as_json})
            return response
        
        return response
    
    def chart_data(self, queryset):
        return (
            queryset.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

    autocomplete_fields = ['unit']
    list_display=['project_name','client','Reactor','work_scope','project_start','project_end','ttds','bdds','calibration_stands',
    'Supply_Orifice',
    "Pressure_Sensor",
    "calibration_stands",
    'created_at',
    # "calibration_orifice",
    "swabmaster",
    "device_Hose",
    'Air_Hose',
    
    'equipment_info_remarks',
    'general_remarks',
    'Last_Comment',]
    
    list_display_links = ['client']
    # 'ttd', 'bdd','calibration_stand'

    fieldsets = [
        ('Project Info', {
            'fields': [ 'project_name','client','unit','reactor','project_number',],
        }),
        (None, {
           
            'fields': ['scope_of_work', 'contract','if_sub_client_name','general_remarks','project_status'],
        }),
        ('Critical Dates', {
           
            'fields': ['equipment_prep', 'equipment_ready','equipment_ship_client','equipment_delivery_client','project_start', 'project_end','equipment_return_tubemaster','equipment_delivery_tubemaster','equipment_info_remarks',],
        }),
        ('Assign Equipment', {
           
            'fields': ['ttd','bdd','calibration_stand',],
        }),

        ('Assign Parts', {
   
            'fields': ['part',"supply_orifice_part","pressure_sensor_part","calibration_orifice_part","swabmaster_part",'device_part',"airhose_part",],
        }),
   
        ]

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
        
    #     if db_field.name == 'ttd':
    #         return TTD.ttdChoiceField(queryset=TTD.objects.all())
            
    #     if db_field.name == 'bdd':
    #         return BDD.bddChoiceField(queryset=BDD.objects.all())
            
    #     if db_field.name == 'calibration_stand':
    #         return CALIBRATION_STAND.calibrationChoiceField(queryset=CALIBRATION_STAND.objects.all())
            
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)
        
            
        
        
    # def save_model(self, request, obj, form, change):
    #     obj.created_by = request.user
    #     super().save_model(request, obj, form, change)

    search_fields = ['client__official_name']
    list_filter = ['client','reactor']
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(ProjectAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['client'].widget.can_add_related = False
        form.base_fields['unit'].widget.can_add_related = False
        form.base_fields['reactor'].widget.can_add_related = False
        return form
admin.site.register(Project,ProjectAdmin)
