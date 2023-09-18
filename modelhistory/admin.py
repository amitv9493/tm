from django.contrib import admin
from .models import EquipmentPartHistory
# Register your models here.

@admin.register(EquipmentPartHistory)
class EquipmentPartHistoryAdmin(admin.ModelAdmin):
    pass
    
