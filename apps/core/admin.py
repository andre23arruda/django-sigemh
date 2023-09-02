from django.contrib import admin
from .models import Location, TechnicalStandard

@admin.register(Location)
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(TechnicalStandard)
class TechnicalStandardAdmin(admin.ModelAdmin):
    list_display = ['title']