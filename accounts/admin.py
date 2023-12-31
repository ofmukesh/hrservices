from django.contrib import admin
from .models import *

@admin.register(Account)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'balance',
                    'contact_no', 'created_on', 'updated_on']
    list_filter = ['balance', 'created_on', 'updated_on']
    search_fields = ['id', 'contact_no']


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'charged', 'balance',
                    'ac', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'ac__contact_no', 'created_on', 'updated_on']


@admin.register(AddMoneyTransactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['id','old_balance', 'money_added', 'balance',
                    'ac', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['id', 'ac__contact_no', 'created_on', 'updated_on']
