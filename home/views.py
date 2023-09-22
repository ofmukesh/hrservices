from django.shortcuts import render,HttpResponse
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from accounts.views import AccountView
from utils.services_api import voter_api

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        print(voter_api(request,'IVG0060012'))
        ac=AccountView().get_account(request)
        if not ac:
            return HttpResponse('account not found!')
        context = {
            'title': settings.PROJECT_NAME,
        }
        return render(request, 'pages/home.html', context=context)
