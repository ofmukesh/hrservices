from django.contrib import admin
from .models import Voterpdf
from accounts.views import AccountView


@admin.register(Voterpdf)
class VoterPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'epic_no',
                    'voter_type', 'file','account', 'status', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on', 'status', 'voter_type']
    search_fields = ['id', 'epic_no', 'account__contact_no']

    def save_model(self, request, obj, form, change):
        voter = Voterpdf.objects.get(id=obj.id)
        ac_id = voter.account.id
        if (voter.status == 'pending' or voter.status == 'success') and obj.status == 'rejected':
            AccountView().reverse_money(ac_id, voter.tid_id)
        if voter.status == 'rejected' and obj.status == 'success':
            AccountView().debit_money(request, voter.tid.charged)
        return super().save_model(request, obj, form, change)
