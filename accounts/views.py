from django.shortcuts import render
from .models import Account, Transactions
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignupForm
from django.contrib.auth.models import User


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
        return ac.balance

    def reverse_money(self, ac_id, tid):
        charge = Transactions.objects.get(id=tid).charged
        ac = Account.objects.get(id=ac_id)
        ac.balance += charge
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


class TransactionsView():
    def add_record(self, request, charge):
        ac = AccountView().get_account(request)
        new = Transactions.objects.create(
            ac=ac, charged=charge, balance=ac.balance)
        new.save()
        return new


class UserTransactionsHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        ac = AccountView().get_account(request)
        transactions = Transactions.objects.filter(
            ac=ac).order_by('-created_on')
        context = {
            'transactions': transactions,
            'title': 'Transactions',
            'table_title': 'Transactions'
        }
        return render(request, 'pages/transactions.html', context=context)


def signup(request):
    msg = ""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Account.objects.create(user=user, balance=0,
                                   contact_no=user.username).save()
            user = User.objects.get(username=user.username)
            user.is_active = False
            user.save()
            print(user.is_active)
            msg = "Your account has successfully registered. To activate your account, kindly contact to site admins."
    else:
        form = SignupForm()
    return render(request, 'pages/sign_up.html', {'form': form, 'msg': msg})
