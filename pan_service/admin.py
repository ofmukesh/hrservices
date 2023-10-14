from django.contrib import admin
from .models import *
from accounts.views import AccountView


@admin.register(InstantPanfind)
class InstantPanFindAdmin(admin.ModelAdmin):
    list_display = ['id', 'aadhar_no','pan_no', 'account', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'aadhar_no', 'account__contact_no']

@admin.register(Panfind)
class PanFindAdmin(admin.ModelAdmin):
    list_display = ['id', 'aadhar_no',
                    'date_of_birth', 'pan_no', 'account', 'status', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'aadhar_no', 'account__contact_no']

    def save_model(self, request, obj, form, change):
        pan = Panfind.objects.get(id=obj.id)
        ac_id = pan.account.id
        if (pan.status == 'pending' or pan.status == 'success') and obj.status == 'rejected':
            AccountView().reverse_money(ac_id, pan.tid_id)
        if pan.status == 'rejected' and obj.status == 'success':
            AccountView().debit_money(request, pan.tid.charged)
        return super().save_model(request, obj, form, change)


@admin.register(Panpdf)
class PanPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'pan_no', 'aadhar_no',
                    'date_of_birth', 'file', 'account', 'status', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'aadhar_no', 'pan_no', 'account__contact_no']

    def save_model(self, request, obj, form, change):
        pan = Panpdf.objects.get(id=obj.id)
        ac_id = pan.account.id
        if (pan.status == 'pending' or pan.status == 'success') and obj.status == 'rejected':
            AccountView().reverse_money(ac_id, pan.tid_id)
        if pan.status == 'rejected' and obj.status == 'success':
            AccountView().debit_money(request, pan.tid.charged)
        return super().save_model(request, obj, form, change)
    
@admin.register(Allpanpdf)
class AllpanpdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name','father_name','pan_no', 'aadhar_no',
                    'date_of_birth','photo','sign', 'file', 'account', 'status', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'aadhar_no', 'pan_no', 'account__contact_no']

    def save_model(self, request, obj, form, change):
        pan = Allpanpdf.objects.get(id=obj.id)
        ac_id = pan.account.id
        if (pan.status == 'pending' or pan.status == 'success') and obj.status == 'rejected':
            AccountView().reverse_money(ac_id, pan.tid_id)
        if pan.status == 'rejected' and obj.status == 'success':
            AccountView().debit_money(request, pan.tid.charged)
        return super().save_model(request, obj, form, change)


@admin.register(AadharToPan)
class AadharToPanAdmin(admin.ModelAdmin):
    list_display = ['id', 'aadhar_no', 'pan_no',
                    'account', 'status', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'aadhar_no', 'pan_no', 'account__contact_no']
