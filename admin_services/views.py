from django.shortcuts import render, HttpResponse
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from utils.services_api import aadhar_to_pan_api
from .forms import VoterRegistrationForm
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
            data = form.cleaned_data
            data['date'] = data['date'].strftime('%d.%m.%Y')
            data['elector_name_hi'] =eth(data['elector_name'])
            data['father_mother_husband_name_hi'] =eth(data['father_mother_husband_name'])
            data['sex_hi'] =eth(data['sex'])
            data['address1_hi'] =eth(data['address1'])
            data['address2_hi'] =eth(data['address2'])
            data['place_hi'] =eth(data['place'])
            print(form['photo'])
            return render(request, 'admin/pages/old_voter.html', context={'title': 'Voter', 'data': data})
        else:
            print(form.errors)
            request.err = "Something went wrong!"
        return self.get(request)
