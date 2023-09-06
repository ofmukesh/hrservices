from django.shortcuts import render
from rest_framework.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'title': settings.PROJECT_NAME,
        }
        return render(request, 'pages/home.html', context=context)
