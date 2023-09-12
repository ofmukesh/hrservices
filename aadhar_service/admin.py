from django.contrib import admin
from .models import Aadharpdf, Aadharfind


@admin.register(Aadharfind)
class AadharFindAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',
                    'enrollment_no', 'time', 'date', 'aadhar_no', 'status', 'account']
    list_filter = ['created_on', 'updated_on','status']
    search_fields = ['id', 'name', 'enrollment_no', 'aadhar_no', 'account__contact_no']


@admin.register(Aadharpdf)
class AadharPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',
                    'enrollment_no', 'time', 'date', 'file', 'status', 'account']
    list_filter = ['created_on', 'updated_on','status']
    search_fields = ['id', 'name', 'enrollment_no', 'aadhar_no', 'account__contact_no']