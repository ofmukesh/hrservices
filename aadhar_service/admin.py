from django.contrib import admin
from .models import Aadharpdf, Aadharfind
from accounts.views import AccountView


@admin.register(Aadharfind)
class AadharFindAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'name',
                    'enrollment_no', 'time', 'date', 'aadhar_no', 'status', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on', 'status']
    search_fields = ['id', 'name', 'enrollment_no',
                     'aadhar_no', 'account__contact_no']

    def save_model(self, request, obj, form, change):
        aadhaar = Aadharfind.objects.get(id=obj.id)
        ac_id=aadhaar.account.id
        if aadhaar.status == 'pending' and obj.status == 'rejected':
            AccountView().reverse_money(ac_id, aadhaar.tid_id)
        if aadhaar.status == 'rejected' and obj.status == 'success':
            AccountView().debit_money(request, aadhaar.tid.charged)
        return super().save_model(request, obj, form, change)


@admin.register(Aadharpdf)
class AadharPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'name',
                    'enrollment_no', 'time', 'date', 'file', 'status', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on', 'status']
    search_fields = ['id', 'name', 'enrollment_no',
                     'aadhar_no', 'account__contact_no']

    def save_model(self, request, obj, form, change):
        aadhar = Aadharpdf.objects.get(id=obj.id)
        ac_id=aadhar.account.id
        if (aadhar.status == 'pending' or aadhar.status == 'success') and obj.status == 'rejected':
            AccountView().reverse_money(ac_id, aadhar.tid_id)
        if aadhar.status == 'rejected' and obj.status == 'success':
            AccountView().debit_money(request, aadhar.tid.charged)
        return super().save_model(request, obj, form, change)
