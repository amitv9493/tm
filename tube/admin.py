from django.contrib import admin
from tube.models import Warehouse

# from tube.models import Activities
# from tube.models import Email
from import_export.admin import ImportExportModelAdmin

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import TruncDay
from django.db.models import Count


class WarehouseAdmin(ImportExportModelAdmin):
    exclude = ["slug"]
    date_hierarchy = "date_created"
    ordering = ["-date_created"]

    def chart_data(self, queryset):
        return (
            queryset.annotate(date=TruncDay("date_created"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        if request.method == "GET":
            queryset = response.context_data["cl"].queryset
            chart_data = self.chart_data(queryset)
            as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
            response.context_data.update({"chart_data": as_json})
            return response

        return response

    import_export_change_list_template = "admin/tube/warehouse/change_list.html"
    list_filter = ["warehouse_location"]
    list_display = (
        "id",
        "warehouse_name",
        "warehouse_location",
        "warehouse_contact",
        "warehouse_email",
        "warehouse_manager",
        "date_created",
    )
    search_fields = ["part_name", "warehouse_name"]


admin.site.register(Warehouse, WarehouseAdmin)
