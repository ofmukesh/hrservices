from django.contrib import admin
from .models import Dlpdf, Dlfind


@admin.register(Dlfind)
class DlFindAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',
                    'father_name', 'state', 'date_of_birth', 'dl_no', 'status', 'account']
    list_filter = ['created_on', 'updated_on','status']
    search_fields = ['id', 'name', 'father_name', 'state', 'dl_no', 'dob']


@admin.register(Dlpdf)
class DlPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'dl_no', 'name_as_per_dl',
                    'date_of_birth', 'file', 'status', 'account']
    list_filter = ['created_on', 'updated_on','status']
    search_fields = ['id', 'name_as_per_dl', 'dl_no']