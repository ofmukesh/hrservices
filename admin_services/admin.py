from django.contrib import admin
from .models import VoterRegistration,InstantPanTransactions

@admin.register(VoterRegistration)
class VoterRegistrationAdmin(admin.ModelAdmin):
    list_display = ['voter_no','photo']


@admin.register(InstantPanTransactions)
class InstantPanTransactionsAdmin(admin.ModelAdmin):
    list_display = ('count', 'created_on', 'updated_on')
    search_fields = ('count',)  # Fields you want to search by
    list_filter = ('created_on', 'updated_on')  # Fields you want to filter by
