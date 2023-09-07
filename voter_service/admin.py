from django.contrib import admin
from .models import Voterpdf

@admin.register(Voterpdf)
class DlPdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'epic_no', 'name_as_voter', 'file', 'status', 'account']
    list_filter = ['created_on', 'updated_on','status']
    search_fields = ['id', 'name_as_voter', 'epic_no']
