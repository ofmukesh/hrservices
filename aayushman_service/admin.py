from django.contrib import admin
from .models import AayushmanPdf
from accounts.views import AccountView

class AayushmanPdfAdmin(admin.ModelAdmin):
    list_display = ('account', 'state', 'parameter_type', 'parameter_no', 'status', 'created_on', 'updated_on')
    list_filter = ('state', 'parameter_type', 'status', 'created_on', 'updated_on')
    search_fields = ('account__user__username', 'account__user__email', 'parameter_no','account__contact_no')

    def save_model(self, request, obj, form, change):
        aayushman = AayushmanPdf.objects.get(id=obj.id)
        ac_id = aayushman.account.id
        if aayushman.status == 'pending' and obj.status == 'rejected':
            AccountView().reverse_money(ac_id, aayushman.tid_id)
        if aayushman.status == 'rejected' and obj.status == 'success':
            AccountView().debit_money(request, aayushman.tid.charged)
        return super().save_model(request, obj, form, change)

admin.site.register(AayushmanPdf, AayushmanPdfAdmin)
