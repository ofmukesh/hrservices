from django.shortcuts import render, HttpResponse
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DlFindForm, DlPdfForm, OtherDlPdfForm
from accounts.views import AccountView,TransactionsView
from services.views import ServiceView
from utils.common import low_balance_err
from .models import Dlfind,Dlpdf,OtherDlpdf


class DlFindView(LoginRequiredMixin, View):
    def get(self, request):
        form = DlFindForm()
        service = ServiceView().get_service_by_id('DL_FIND')
        return render(request, 'services/dl/dl_find.html', context={'title': 'Find DL', 'form': form, 'service': service})

    def post(self, request):
        form = DlFindForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('DL_FIND')

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


class DlPdfView(LoginRequiredMixin, View):
    def get(self, request):
        form = DlPdfForm()
        service = ServiceView().get_service_by_id('DL_PDF')
        return render(request, 'services/dl/dl_pdf.html', context={'title': 'Pdf DL', 'form': form, 'service': service})

    def post(self, request):
        form = DlPdfForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('DL_PDF')

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


class OtherDlPdfView(LoginRequiredMixin, View):
    def get(self, request):
        form = OtherDlPdfForm()
        service = ServiceView().get_service_by_id('OTHER_DL_PDF')
        return render(request, 'services/dl/other_dl_pdf.html', context={'title': 'Other State DL', 'form': form, 'service': service})

    def post(self, request):
        form = OtherDlPdfForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('OTHER_DL_PDF')

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

class DlFindRecordView(LoginRequiredMixin,View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Dlfind.objects.filter(account=ac)
        context = {
            'title': 'DL Number Find Record',
            'records': records,
            'table_title': 'DL Number Find Record'
        }
        return render(request, 'services/dl/dl_records.html', context=context)



class DlPdfRecordView(LoginRequiredMixin,View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Dlpdf.objects.filter(account=ac)
        context = {
            'title': 'DL PDF Record',
            'records': records,
            'table_title': 'DL PDF Record'
        }
        return render(request, 'services/dl/dl_pdf_records.html', context=context)
    

class OtherDlPdfRecordView(LoginRequiredMixin,View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = OtherDlpdf.objects.filter(account=ac)
        context = {
            'title': 'Other DL PDF Record',
            'records': records,
            'table_title': 'Other DL PDF Record'
        }
        return render(request, 'services/dl/other_dl_pdf_records.html', context=context)