from django.shortcuts import render, HttpResponse
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NsdlPanFindForm, PanPdfForm
from accounts.views import AccountView
from services.views import ServiceView
from utils.common import low_balance_err
from .models import Nsdlpanfind,Panpdf


class NsdlPanFindView(LoginRequiredMixin, View):
    def get(self, request):
        form = NsdlPanFindForm()
        service = ServiceView().get_service_by_id('PAN_FIND')
        return render(request, 'services/pan/nsdl_pan_find.html', context={'title': 'Find Pan', 'form': form, 'service': service})

    def post(self, request):
        form = NsdlPanFindForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('PAN_FIND')

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


class PanPdfView(LoginRequiredMixin, View):
    def get(self, request):
        form = PanPdfForm()
        service = ServiceView().get_service_by_id('PAN_PDF')
        return render(request, 'services/pan/pan_pdf.html', context={'title': 'Pdf Pan', 'form': form, 'service': service})

    def post(self, request):
        form = PanPdfForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('PAN_PDF')

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


class NsdlPanFindRecordView(View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Nsdlpanfind.objects.filter(account=ac)
        context = {
            'title': 'NSDL | PAN Number Find Record',
            'records': records,
            'table_title': 'NSDL | PAN Number Find Record'
        }
        return render(request, 'services/pan/nsdl_records.html', context=context)



class PanPdfRecordView(View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Panpdf.objects.filter(account=ac)
        context = {
            'title': 'Pancard PDF Record',
            'records': records,
            'table_title': 'Pancard PDF Record'
        }
        return render(request, 'services/pan/pdf_records.html', context=context)