from django.shortcuts import render, HttpResponse
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import VoterPdfForm
from accounts.views import AccountView,TransactionsView
from services.views import ServiceView
from utils.common import low_balance_err
from .models import Voterpdf

class VoterPdfView(LoginRequiredMixin, View):
    def get(self, request):
        form = VoterPdfForm()
        service = ServiceView().get_service_by_id('VOTER_PDF')
        return render(request, 'services/voter/voter_pdf.html', context={'title': 'Pdf Voter', 'form': form, 'service': service})

    def post(self, request):
        form = VoterPdfForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('VOTER_PDF')

        if ac is None:
            return HttpResponse('Account not found')
        elif service.charge > ac.balance:
            request.err = low_balance_err
        elif form.is_valid():
            AccountView().debit_money(request, service.charge)
            form.instance.tid=TransactionsView().add_record(request,service.charge)
            form.save()  # saving the data
            request.msg = "Successfully submitted!"
        else:
            request.err = "Something went wrong!"
        return self.get(request)

class VoterPdfRecordView(LoginRequiredMixin,View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Voterpdf.objects.filter(account=ac)
        context = {
            'title': 'Voter PDF Record',
            'records': records,
            'table_title': 'Voter PDF Record'
        }
        return render(request, 'services/voter/voter_pdf_records.html', context=context)