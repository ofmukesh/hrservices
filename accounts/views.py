from django.shortcuts import render
from .models import Account
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class AccountView():
    def get_account(self, request):
        ac = None
        if Account.objects.filter(user=request.user).exists():
            ac = Account.objects.get(user=request.user)
        return ac

    def debit_money(self, request, charge):
        ac = self.get_account(request)
        ac.balance -= charge
        ac.save()

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        ac = AccountView().get_account(request)
        context = {
            'ac': ac,
            'title': 'Profile'
        }
        return render(request, 'pages/profile.html', context=context)


class WalletView(LoginRequiredMixin, View):
    def get(self, request):
        balance = AccountView().get_account(request).balance
        context = {
            'balance': balance,
            'title': 'Wallet'
        }
        return render(request, 'pages/wallet.html', context=context)


# def reject_application(request):
