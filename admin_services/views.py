from django.shortcuts import render, HttpResponse
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from utils.services_api import aadhar_to_pan_api
from .forms import VoterRegistrationForm,VoterRegistration
from eng_hindi import eth
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
            return render(request, 'admin/pages/old_voter.html', context={'title': 'Voter', 'data': data})
        else:
            request.err = form.errors
        return self.get(request)
