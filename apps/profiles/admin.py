from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, JobTitle


class ProfileInline(admin.StackedInline):
    can_delete = False
    max_num = 1
    model = Profile
    verbose_name = 'Profile'
    verbose_name_plural = 'Profile'


class UserRegister(UserAdmin):
    inlines = [ProfileInline]
    list_filter = ['is_active']
    search_fields = ['username', 'email']

    class Media:
        css = {'all': ('css/stacked-inline.css',)}


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_display_links = ['name']
    ordering = ['name']


admin.site.unregister(User)
admin.site.register(User, UserRegister)