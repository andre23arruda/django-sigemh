from django.contrib import admin
from .models import WorkOrder


@admin.register(WorkOrder)
class WorkOrderTypeAdmin(admin.ModelAdmin):
    list_display = ['service', 'checkin', 'status']
