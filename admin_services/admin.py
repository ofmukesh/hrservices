from django.contrib import admin
from .models import VoterRegistration

@admin.register(VoterRegistration)
class VoterRegistrationAdmin(admin.ModelAdmin):
    list_display = ['voter_no', 'elector_name', 'sex', 'age', 'place', 'date_of_registration']
    list_filter = ['sex', 'place']
    search_fields = ['voter_no', 'elector_name', 'place']
