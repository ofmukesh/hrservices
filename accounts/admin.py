from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'balance', 'contact_no']
    list_filter = ['balance', 'created_on', 'updated_on']
    search_fields = ['id','contact_no']
