from django.contrib import admin
from .models import Nsdlpanfind, Panpdf


@admin.register(Nsdlpanfind)
class NsdlPanFindAdmin(admin.ModelAdmin):
    list_display = ['id', 'aadhar_no',
                    'name_as_pan', 'date_of_birth', 'pan_no', 'status','account']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'aadhar_no', 'name_as_pan', 'dob']


@admin.register(Panpdf)
class PanPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'pan_no', 'aadhar_no', 'date_of_birth','file', 'status','account']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'aadhar_no', 'pan_no', 'dob']