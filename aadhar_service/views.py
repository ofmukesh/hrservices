from django.shortcuts import render, HttpResponse
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AadharFindForm, AadharPdfForm
from accounts.views import AccountView,TransactionsView
from services.views import ServiceView
from utils.common import low_balance_err
from .models import Aadharfind, Aadharpdf


class AadharFindView(LoginRequiredMixin, View):
    def get(self, request):
        form = AadharFindForm()
        service = ServiceView().get_service_by_id('AADHAR_FIND')
        return render(request, 'services/aadhar/aadhar_find.html', context={'title': 'Find Aadhar by EID', 'form': form, 'service': service})

    def post(self, request):
        form = AadharFindForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('AADHAR_FIND')

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


class AadharPdfView(LoginRequiredMixin, View):
    def get(self, request):
        form = AadharPdfForm()
        service = ServiceView().get_service_by_id('AADHAR_PDF')
        return render(request, 'services/aadhar/aadhar_pdf.html', context={'title': 'Pdf Aadhar', 'form': form, 'service': service})

    def post(self, request):
        form = AadharPdfForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('AADHAR_PDF')

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


class AadharFindRecordView(LoginRequiredMixin,View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Aadharfind.objects.filter(account=ac)
        context = {
            'title': 'EID | Aadhar Number Find Record',
            'records': records,
            'table_title': 'EID | Aadhar Number Find Record'
        }
        return render(request, 'services/aadhar/aadhar_records.html', context=context)


class AadharPdfRecordView(LoginRequiredMixin,View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Aadharpdf.objects.filter(account=ac)
        context = {
            'title': 'Aadhar PDF Record',
            'records': records,
            'table_title': 'Aadhar PDF Record'
        }
        return render(request, 'services/aadhar/aadhar_pdf_records.html', context=context)
