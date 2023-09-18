from django.shortcuts import render, HttpResponse
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from .forms import *
from accounts.views import AccountView,TransactionsView
from services.views import ServiceView
from utils.common import low_balance_err
from .models import Panfind, Panpdf
from utils.services_api import aadhar_to_pan_api


class InstantPanFindView(LoginRequiredMixin, View):
    def get(self, request):
        form = InstantPanFindForm()
        service = ServiceView().get_service_by_id('INSTANT_PAN_FIND')
        return render(request, 'services/pan/instant_pan_find.html', context={'title': 'Instant Find Pan', 'form': form, 'service': service})

    def post(self, request):
        form = InstantPanFindForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('INSTANT_PAN_FIND')

        if ac is None:
            return HttpResponse('Account not found')
        elif service.charge > ac.balance:
            request.err = low_balance_err
        elif form.is_valid():
            res=aadhar_to_pan_api(request,form.instance.aadhar_no)
            if res.get('pan_no'):
                AccountView().debit_money(request, service.charge)
                form.instance.tid=TransactionsView().add_record(request,service.charge)
                form.instance.pan_no=res['pan_no']
                form.save()  # saving the data
                request.msg = "Pan no. found check list!"
            elif res.get('status') and res['status']=="Fail to Login":
                request.err = "Wrong data submitted!"
            else:
                request.err = res['message']
        else:
            request.err = "Something went wrong!"
        return self.get(request)

class NsdlPanFindView(LoginRequiredMixin, View):
    def get(self, request):
        form = PanFindForm()
        service = ServiceView().get_service_by_id('PAN_FIND')
        return render(request, 'services/pan/pan_find.html', context={'title': 'Find Pan', 'form': form, 'service': service})

    def post(self, request):
        form = PanFindForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('PAN_FIND')

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
    

class UtiPanPdfView(LoginRequiredMixin, View):
    def get(self, request):
        form = UtiPanPdfForm()
        service = ServiceView().get_service_by_id('UTI_PAN_PDF')
        return render(request, 'services/pan/uti_pan_pdf.html', context={'title': 'UTI PAN PDF', 'form': form, 'service': service})

    def post(self, request):
        form = UtiPanPdfForm(request.POST,request.FILES)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('UTI_PAN_PDF')

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
            AccountView().debit_money(request, service.charge)
            form.instance.tid=TransactionsView().add_record(request,service.charge)
            form.save()  # saving the data
            request.msg = "Successfully submitted!"
        else:
            request.err = "Something went wrong!"
        return self.get(request)


class NsdlPanFindRecordView(LoginRequiredMixin, View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Panfind.objects.filter(account=ac)
        context = {
            'title': 'Find Record',
            'records': records,
            'table_title': 'PAN Number Find Record'
        }
        return render(request, 'services/pan/pan_records.html', context=context)


class PanPdfRecordView(LoginRequiredMixin, View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Panpdf.objects.filter(account=ac)
        context = {
            'title': 'PDF Record',
            'records': records,
            'table_title': 'Pancard PDF Record'
        }
        return render(request, 'services/pan/pdf_records.html', context=context)
    

class UtiPanPdfRecordView(LoginRequiredMixin, View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = Utipanpdf.objects.filter(account=ac)
        context = {
            'title': 'UTI PDF Record',
            'records': records,
            'table_title': 'UTI PAN PDF Record'
        }
        return render(request, 'services/pan/uti_records.html', context=context)
    

class InstantPanRecordView(LoginRequiredMixin, View):
    def get(self, request):
        ac = AccountView().get_account(request)
        records = InstantPanfind.objects.filter(account=ac)
        context = {
            'title': 'INSTANT PAN RECORD',
            'records': records,
            'table_title': 'INSTANT PAN RECORD'
        }
        return render(request, 'services/pan/instant_pan_records.html', context=context)


# admin services
class AadharToPanView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        form = AadharToPanForm()
        return render(request, 'admin/pages/aadhar_to_pan.html', context={'title': 'Aadhar to Pan', 'form': form})

    def post(self, request):
        form = AadharToPanForm(request.POST)  # form data from request
        ac = AccountView().get_account(request)
        form.instance.account = ac
        service = ServiceView().get_service_by_id('PAN_FIND')

        if form.is_valid():
            result=aadhar_to_pan_api(request,form.instance.aadhar_no)
            request.result=result
            request.msg = "Pan no. found!"
        
        else:
            request.err = "Something went wrong!"
        return self.get(request)
