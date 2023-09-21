from django.shortcuts import render
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from utils.services_api import aadhar_to_pan_api
from .forms import VoterRegistrationForm,VoterRegistration
from eng_hindi import eth
from pan_service.forms import AadharToPanForm
import uuid

class AdminView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        context = {
            'title': 'Admin'
        }
        return render(request, 'admin/home.html', context=context)


class VoterMakerView(LoginRequiredMixin, AccessMixin, View):
    def get(self, request):
        form = VoterRegistrationForm()
        return render(request, 'admin/forms/voter_reg.html', context={'title': 'Covid', 'form': form})

    def post(self, request):
        form = VoterRegistrationForm(request.POST,request.FILES)  # form data from request
        if form.is_valid():
            form.save()
            data=VoterRegistration.objects.get(id=form.instance.id)
            data.date = data.date_of_registration.strftime('%d.%m.%Y')
            data.elector_name_hi =eth(data.elector_name)
            data.father_mother_husband_name_hi =eth(data.father_mother_husband_name)
            data.sex_hi =eth(data.sex)
            data.address1_hi =eth(data.address1)
            data.address2_hi =eth(data.address2)
            data.place_hi =eth(data.place)
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
            result=aadhar_to_pan_api(request,form.instance.aadhar_no,"admin_call"+uuid.uuid4().hex[:10])
            request.result=result
            request.msg = "Pan no. found!"
        else:
            request.err = "Something went wrong"
        
        return self.get(request)
