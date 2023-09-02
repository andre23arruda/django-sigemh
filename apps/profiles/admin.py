from django.contrib import admin
from .models import Profile, JobTitle


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'job_title', 'engineering_team']
    list_display_links = ['user']


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_display_links = ['name']
    ordering = ['name']
