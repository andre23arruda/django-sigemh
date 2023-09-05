from django.contrib import admin
from .models import Equipment, EquipmentModel, EquipmentType, Manufacturer


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['patrimony', 'equipment_model', 'show_qr_code']
    readonly_fields = ['qr_code']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.save_qr_code()


@admin.register(EquipmentModel)
class EquipmentModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']
