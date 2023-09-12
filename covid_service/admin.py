from django.contrib import admin
from .models import Covid
from accounts.views import AccountView


@admin.register(Covid)
class CovidAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile_no',
                    'aadhar_no', 'date_of_birth', 'gender', 'status', 'account','created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on', 'status']
    search_fields = ['id', 'name', 'aadhar_no', 'mobile_no', 'account__contact_no']


    def save_model(self, request, obj, form, change):
        conid=Covid.objects.get(id=obj.id)
        if conid.status=='pending'  and obj.status=='rejected':
            AccountView().reverse_money(request,conid.tid_id)
        if conid.status=='rejected'  and obj.status=='success':
            AccountView().debit_money(request,conid.tid.charged)
        return  super().save_model(request, obj, form, change)