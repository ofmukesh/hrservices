from django.contrib import admin
from .models import VoterRegistration

@admin.register(VoterRegistration)
class VoterRegistrationAdmin(admin.ModelAdmin):
    list_display = ['voter_no','photo']
