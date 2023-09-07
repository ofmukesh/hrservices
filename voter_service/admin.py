from django.contrib import admin
from .models import Voterpdf


@admin.register(Voterpdf)
class VoterPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'epic_no', 'name_as_voter',
                    'voter_type', 'file', 'status', 'account']
    list_filter = ['created_on', 'updated_on', 'status', 'voter_type']
    search_fields = ['id', 'name_as_voter', 'epic_no']
