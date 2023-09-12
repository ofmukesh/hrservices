from django.contrib import admin
from .models import Panfind, Panpdf,AadharToPan


@admin.register(Panfind)
class PanFindAdmin(admin.ModelAdmin):
    list_display = ['id', 'aadhar_no',
                    'date_of_birth', 'pan_no', 'status', 'account','created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'aadhar_no', 'account__contact_no']


@admin.register(Panpdf)
class PanPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'pan_no', 'aadhar_no',
                    'date_of_birth', 'file', 'status', 'account','created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'aadhar_no', 'pan_no', 'account__contact_no']


@admin.register(AadharToPan)
class AadharToPanAdmin(admin.ModelAdmin):
    list_display = ['id', 'aadhar_no','pan_no', 'status', 'account','created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'aadhar_no', 'pan_no', 'account__contact_no']
