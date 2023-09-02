from django.contrib import admin
from .models import Requester, Provider, Category, Product, Checkin, Checkout


@admin.register(Requester)
class RequesterTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Checkin)
class CheckinAdmin(admin.ModelAdmin):
    list_display = ['product', 'date']


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['product', 'date']
