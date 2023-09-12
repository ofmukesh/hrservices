from django.contrib import admin
from .models import Covid


@admin.register(Covid)
class CovidAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile_no',
                    'aadhar_no', 'date_of_birth', 'gender', 'status', 'account']
    list_filter = ['created_on', 'updated_on', 'status']
    search_fields = ['id', 'name', 'aadhar_no', 'mobile_no', 'account__contact_no']
