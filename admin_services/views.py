# Import necessary modules and classes
from django.shortcuts import render, redirect
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from utils.services_api import aadhar_to_pan_api
from .forms import *
from .models import *
from pan_service.forms import AadharToPanForm
import uuid
from accounts.models import Account, AddMoneyTransactions, Transactions
from django.utils import timezone
from django.db.models import Sum
from utils.services_api import voter_api
from eng_hindi import eth

# Define an AdminView class with GET and POST methods for handling admin homepage
class AdminView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        context = {
            'title': 'Home | Admin',
        }
        return render(request, 'admin/home.html', context=context)

    def post(self, request):
        # Handle POST request to search for a user
        form = SearchUserForm(request.POST)
        try:
            # Attempt to retrieve an account based on mobile number
            ac = Account.objects.get(
                contact_no=form['mobile_no'].value())
            return redirect(f'user/{ac.id}')
        except:
            request.err = "Not found"
        return self.get(request)

# Define a ServicesView class with GET method for displaying services page
class ServicesView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        context = {
            'title': 'Services | Admin',
        }
        return render(request, 'admin/pages/services.html', context=context)

# Define a DashboardView class with GET method for displaying admin dashboard
class DashboardView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        # Chart data for the last 10 days
        days = 10

        # Get today's date
        seven_days_ago = timezone.now() - timezone.timedelta(days=days)

        # Initialize chart data
        chart_data = {'dates': [], 'money_added': [], 'transactions': []}

        # Loop through the last 7 days to collect data
        for i in range(days+1):
            day = seven_days_ago + timezone.timedelta(days=i)
            day_end = day + timezone.timedelta(days=1)

            # Query to retrieve the money added for the current day
            money_added = AddMoneyTransactions.objects.filter(
                created_on__gte=day,
                created_on__lt=day_end
            ).aggregate(Sum('money_added'))['money_added__sum']

            transaction = Transactions.objects.filter(
                created_on__gte=day,
                created_on__lt=day_end
            ).aggregate(Sum('charged'))['charged__sum']

            # If there is no data for the current day, set money_added to 0
            if money_added is None:
                money_added = 0

            if transaction is None:
                transaction = 0

            chart_data['dates'].append(day.strftime("%Y-%m-%d"))
            chart_data['money_added'].append(money_added)
            chart_data['transactions'].append(transaction)

        # Calculate the sum of current_total for non-superusers
        total_balance = Account.objects.filter(user__is_superuser=False).aggregate(
            Sum('balance'))['balance__sum']

        # Check if the total_balance is None (no non-superusers found) and set it to 0 if needed
        total_balance = total_balance if total_balance is not None else 0

        # instant pan api used count
        today = date.today()
        count_used_instantpan = InstantPanTransactions.objects.filter(created_on__date=today).first().count if InstantPanTransactions.objects.filter(created_on__date=today) else 0

        context = {
            'title': 'Dashboard | Admin',
            'values': chart_data,
            'total_balance': total_balance,
            'count_used_pan_service':count_used_instantpan,
        }

        return render(request, 'admin/pages/dashboard.html', context=context)

# Define an AddMoneyView class with GET and POST methods for adding money to a user's account
class AddMoneyView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        context = {
            'title': 'Services | Admin',
            'serchUserForm': SearchUserForm(),
        }
        return render(request, 'admin/pages/add_money.html', context=context)

    def post(self, request):
        # Handle POST request to search for a user
        form = SearchUserForm(request.POST)
        try:
            # Attempt to retrieve an account based on mobile number
            ac = Account.objects.get(
                contact_no=form['mobile_no'].value())
            return redirect(f'../user/{ac.id}')
        except:
            request.err = "Not found"
        return self.get(request)

# Define a UserProfile class with GET and POST methods for displaying and updating user profiles
class UserProfile(LoginRequiredMixin, AccessMixin, View):
    def get(self, request, pk):
        ac = Account.objects.get(id=pk)
        context = {
            'title': 'User Profile',
            'user': ac,
            'addMoneyForm': AddMoneyForm(),
        }
        return render(request, 'admin/pages/user_profile.html', context=context)

    def post(self, request, pk):
        form = AddMoneyForm(request.POST)
        ac = Account.objects.get(id=pk)
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

# Define a VoterMakerView class with GET and POST methods for generating voter registrations
class VoterMakerView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        form = VoterRegistrationForm()
        return render(request, 'admin/forms/voter_reg.html', context={'title': 'Voter Generate', 'form': form})

    def post(self, request):
        form = VoterRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            tmp_data = VoterRegistration.objects.get(id=form.instance.id)
            try:
                data = voter_api(request, tmp_data.voter_no)[
                    'response']['docs'][0]
            except:
                data = {}
            data['pic'] = tmp_data.photo
            data['date'] = timezone.now().strftime("%d/%m/%Y")
            data['state_v1'] = eth(data.get('state', ''))
            data['address1'] = tmp_data.address1
            data['address1_v1'] = eth(tmp_data.address1)
            return render(request, 'admin/pages/latest_voter.html', context={'title': 'Voter', 'data': data})
        else:
            request.err = form.errors
        return self.get(request)

# Define an AadharToPanView class with GET and POST methods for converting Aadhar to PAN
class AadharToPanView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        form = AadharToPanForm()
        return render(request, 'admin/pages/aadhar_to_pan.html', context={'title': 'Aadhar to Pan', 'form': form})

    def post(self, request):
        form = AadharToPanForm(request.POST)
        if form.is_valid():
            result = aadhar_to_pan_api(
                request, form.instance.aadhar_no, "admin_call" + uuid.uuid4().hex[:10])
            request.result = result
            try:
                request.msg = "Pan no. found!"  if result['status'] else None
                InstantPanTransactions.create_or_update_transaction()
            except:
                request.err = result['message']
        else:
            request.err = "Something went wrong"
        return self.get(request)

# Define an OldVoterMakerView class with GET and POST methods for generating old voter registrations
class OldVoterMakerView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        form = VoterRegistrationOldForm()
        return render(request, 'admin/forms/old_voter_reg.html', context={'title': 'Old Voter Generate', 'form': form})

    def post(self, request):
        form = VoterRegistrationOldForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = VoterRegistrationOld.objects.get(id=form.instance.id)
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
