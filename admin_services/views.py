from django.shortcuts import render, redirect
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from utils.services_api import aadhar_to_pan_api
from .forms import *
from eng_hindi import eth
from pan_service.forms import AadharToPanForm
import uuid
from accounts.models import Account, AddMoneyTransactions


class AdminView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        context = {
            'title': 'Admin',
            'serchUserForm': SearchUserForm(),
        }
        return render(request, 'admin/home.html', context=context)

    def post(self, request):
        form = SearchUserForm(request.POST)
        try:
            ac = Account.objects.get(
                contact_no=form['mobile_no'].value())
            return redirect(f'user/{ac.id}')
        except:
            request.err = "Not found"
        return self.get(request)


class UserProfile(LoginRequiredMixin, AccessMixin, View):
    def get(self, request, pk):
        ac = Account.objects.get(
            id=pk)
        context = {
            'title': 'User Profile',
            'user': ac,
            'addMoneyForm': AddMoneyForm(),
        }
        return render(request, 'admin/pages/user_profile.html', context=context)

    def post(self, request, pk):
        form = AddMoneyForm(request.POST)
        ac = Account.objects.get(
            id=pk)
        add_amount = int(form['amount'].value())
        if form.is_valid() and add_amount > 0:
            old_balance = ac.balance
            ac.balance += add_amount
            ac.save()
            transaction = AddMoneyTransactions.objects.create(old_balance=old_balance,
                                                              ac=ac, money_added=add_amount, balance=ac.balance)
            transaction.save()
            request.msg = f"Amount {add_amount} added successfully! transcation id is {transaction.id}"
        elif add_amount < 0:
            request.err = "enter amount more than 0"
        else:
            request.err = "Something went wrong"
        return self.get(request, pk)


class VoterMakerView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        form = VoterRegistrationForm()
        return render(request, 'admin/forms/voter_reg.html', context={'title': 'Voter Generate', 'form': form})

    def post(self, request):
        form = VoterRegistrationForm(
            request.POST, request.FILES)  # form data from request
        if form.is_valid():
            form.save()
            data = VoterRegistration.objects.get(id=form.instance.id)
            data.date = data.date_of_registration.strftime('%d.%m.%Y')
            data.elector_name_hi = eth(data.elector_name)
            data.father_mother_husband_name_hi = eth(
                data.father_mother_husband_name)
            data.sex_hi = eth(data.sex)
            data.address1_hi = eth(data.address1)
            data.address2_hi = eth(data.address2)
            data.place_hi = eth(data.place)
            return render(request, 'admin/pages/old_voter.html', context={'title': 'Voter', 'data': data})
        else:
            request.err = form.errors
        return self.get(request)


class AadharToPanView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        form = AadharToPanForm()
        return render(request, 'admin/pages/aadhar_to_pan.html', context={'title': 'Aadhar to Pan', 'form': form})

    def post(self, request):
        form = AadharToPanForm(request.POST)
        if form.is_valid():
            result = aadhar_to_pan_api(
                request, form.instance.aadhar_no, "admin_call"+uuid.uuid4().hex[:10])
            request.result = result
            request.msg = "Pan no. found!"
        else:
            request.err = "Something went wrong"

        return self.get(request)
