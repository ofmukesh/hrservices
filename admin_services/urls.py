from django.urls import path
from .views import *

urlpatterns = [
    path('', AdminView.as_view(),name='home_admin'),
    path('dashboard/', DashboardView.as_view(),name='dashboard_admin'),
    path('services/', ServicesView.as_view(),name='services_admin'),
    path('add_money/', AddMoneyView.as_view(),name='add_money_admin'),
    path('user/<int:pk>', UserProfile.as_view(),name='user_profile'),
    path('aadhar_to_pan/', AadharToPanView.as_view(),name='aadhar_to_pan'),
    path('voter_gen/', VoterMakerView.as_view(),name='voter_gen'),
]