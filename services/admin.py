from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'charge', 'isActive']
    list_filter = ['isActive','created_on', 'updated_on']
    search_fields = ['id','name', 'account']