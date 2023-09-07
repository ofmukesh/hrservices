from django.shortcuts import render, HttpResponse
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CovidForm
from accounts.views import AccountView
from services.views import ServiceView
from utils.common import low_balance_err
from .models import Covid

class CovidView(LoginRequiredMixin, View):
    def get(self, request):
        form = CovidForm()
        service = ServiceView().get_service_by_id('COVID')
        return render(request, 'services/covid/covid.html', context={'title': 'Covid', 'form': form, 'service': service})

    def post(self, request):
        form = CovidForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('COVID')

        if ac is None:
            return HttpResponse('Account not found')
        elif service.charge > ac.balance:
            request.err = low_balance_err
        elif form.is_valid():
            form.save()  # saving the data
            AccountView().debit_money(request, service.charge)
            request.msg = "Successfully submitted!"
        else:
            request.err = "Something went wrong!"
        return self.get(request)

class CovidRecordView(View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Covid.objects.filter(account=ac)
        context = {
            'title': 'Covid Record',
            'records': records,
            'table_title': 'Covid Record'
        }
        return render(request, 'services/covid/covid_records.html', context=context)