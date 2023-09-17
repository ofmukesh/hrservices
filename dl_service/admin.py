from django.contrib import admin
from .models import Dlpdf, Dlfind
from accounts.views import AccountView


@admin.register(Dlfind)
class DlFindAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',
                    'father_name', 'state', 'date_of_birth', 'dl_no', 'account', 'status', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on', 'status']
    search_fields = ['id', 'name', 'father_name',
                     'state', 'dl_no', 'dob', 'account__contact_no']

    def save_model(self, request, obj, form, change):
        dl = Dlfind.objects.get(id=obj.id)
        ac_id = dl.account.id
        if (dl.status == 'pending' or dl.status == 'success') and obj.status == 'rejected':
            AccountView().reverse_money(ac_id, dl.tid_id)
        if dl.status == 'rejected' and obj.status == 'success':
            AccountView().debit_money(request, dl.tid.charged)
        return super().save_model(request, obj, form, change)


@admin.register(Dlpdf)
class DlPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'dl_no', 'name_as_per_dl',
                    'date_of_birth', 'file', 'account', 'status', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on', 'status']
    search_fields = ['id', 'name_as_per_dl', 'dl_no', 'account__contact_no']

    def save_model(self, request, obj, form, change):
        dl = Dlpdf.objects.get(id=obj.id)
        ac_id = dl.account.id
        if (dl.status == 'pending' or dl.status == 'success') and obj.status == 'rejected':
            AccountView().reverse_money(ac_id, dl.tid_id)
        if dl.status == 'rejected' and obj.status == 'success':
            AccountView().debit_money(request, dl.tid.charged)
        return super().save_model(request, obj, form, change)
