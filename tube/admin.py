from django.contrib import admin
from tube.models import Catalyst
from tube.models import Warehouse
# from tube.models import Activities
# from tube.models import Email
from tube.models import Loading
from import_export.admin import ImportExportMixin, ImportExportModelAdmin
# from tube.models import Comments
# Register your models here.



import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import TruncDay
from django.db.models import Count


@admin.register(Loading)
class LoadingAdmin(admin.ModelAdmin):





    
    list_display=['catalyst_to_be_loaded',
                 'layers_of_catalyst',
                 'layers_of_inerts',
                 'loaded_tube_length_in',
                 'loaded_tube_length_mm',
                 'tube_bottom_retainer',
                 'top_spring',
                 'spring_height',
                 'spring_drawing',
                 ]
    list_filter=['catalyst_to_be_loaded']

    search_fields = [
        'catalyst_to_be_loaded',

    ]    



      
@admin.register(Catalyst)
class CatalystAdmin(admin.ModelAdmin):
    list_filter=['manufacturer',]
    list_display = [
        'catalyst_name',
        'manufacturer',

    ]
    search_fields = [
        'catalyst_name',
        'manufacturer',
    ]
    




class WarehouseAdmin(ImportExportModelAdmin):
    date_hierarchy = "date_created"
    ordering = ['-date_created']
    
    def chart_data(self, queryset):
        return (
            queryset.annotate(date=TruncDay("date_created"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )
        

    def changelist_view(self, request, extra_context=None):
        if request.method == "GET":
            response = super().changelist_view(request, extra_context=extra_context)
            queryset = response.context_data["cl"].queryset
            chart_data = self.chart_data(queryset)
            as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
            response.context_data.update({"chart_data": as_json})
            return response
            
        return response
    

    import_export_change_list_template = 'admin/tube/warehouse/change_list.html'
    list_filter=['warehouse_location']
    list_display = ('warehouse_name', 'warehouse_location','warehouse_contact',
    'warehouse_email', 'warehouse_manager','date_created',)
    search_fields = ['part_name','warehouse_name']
    
admin.site.register(Warehouse,WarehouseAdmin)


