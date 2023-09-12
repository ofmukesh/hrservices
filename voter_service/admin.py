from django.contrib import admin
from .models import Voterpdf
from accounts.views import AccountView

@admin.register(Voterpdf)
class VoterPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'epic_no', 'name_as_voter',
                    'voter_type', 'file', 'status', 'account','created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on', 'status', 'voter_type']
    search_fields = ['id', 'name_as_voter', 'epic_no', 'account__contact_no']

    def save_model(self, request, obj, form, change):
        voter=Voterpdf.objects.get(id=obj.id)
        if (voter.status=='pending' or voter.status=='success')  and obj.status=='rejected':
            AccountView().reverse_money(request,voter.tid_id)
        if voter.status=='rejected'  and obj.status=='success':
            AccountView().debit_money(request,voter.tid.charged)
        return  super().save_model(request, obj, form, change)