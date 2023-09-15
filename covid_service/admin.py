from django.contrib import admin
from .models import Covid
from accounts.views import AccountView


@admin.register(Covid)
class CovidAdmin(admin.ModelAdmin):
    list_display = ['id','account', 'name', 'mobile_no',
                    'aadhar_no', 'date_of_birth', 'gender', 'status', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on', 'status']
    search_fields = ['id', 'name', 'aadhar_no',
                     'mobile_no', 'account__contact_no']

    def save_model(self, request, obj, form, change):
        covid = Covid.objects.get(id=obj.id)
        ac_id=covid.account.id
        if (covid.status == 'pending' or covid.status == 'success') and obj.status == 'rejected':
            AccountView().reverse_money(ac_id, covid.tid_id)
        if covid.status == 'rejected' and obj.status == 'success':
            AccountView().debit_money(request, covid.tid.charged)
        return super().save_model(request, obj, form, change)
