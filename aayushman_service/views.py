from django.shortcuts import render, HttpResponse
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AayushmanPdfForm ,AayushmanPdf 
from accounts.views import AccountView
from services.views import ServiceView
from utils.common import low_balance_err
from accounts.views import TransactionsView 


class AayushmanPdfView(LoginRequiredMixin, View):
    def get(self, request):
        form = AayushmanPdfForm()  
        service = ServiceView().get_service_by_id('AAYUSHMAN_PDF')  
        return render(request, 'services/aayushman/aayushman_pdf.html', context={'title': 'Aayushman Card Pdf', 'form': form, 'service': service})

    def post(self, request):
        form = AayushmanPdfForm(request.POST)  
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('AAYUSHMAN_PDF')  

        if ac is None:
            return HttpResponse('Account not found')
        elif service.charge > ac.balance:
            request.err = low_balance_err
        elif form.is_valid():
            AccountView().debit_money(request, service.charge)
            form.instance.tid = TransactionsView().add_record(request, service.charge)  # If you have a TransactionsView
            form.save()  # saving the data
            request.msg = "Successfully submitted!"
        else:
            request.err = "Something went wrong!"
        return self.get(request)


class AayushmanPdfRecordView(LoginRequiredMixin,View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = AayushmanPdf.objects.filter(account=ac)
        context = {
            'title': 'Aayushman Card PDF Record',
            'records': records,
            'table_title': 'Aayushman Card PDF Record'
        }
        return render(request, 'services/aayushman/aayushman_pdf_records.html', context=context)