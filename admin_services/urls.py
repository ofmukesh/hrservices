from django.urls import path
from .views import *

urlpatterns = [
    path('', AdminView.as_view(),name='home_admin'),
    path('user/<int:pk>', UserProfile.as_view(),name='user_profile'),
    path('aadhar_to_pan/', AadharToPanView.as_view(),name='aadhar_to_pan'),
    path('voter_gen/', VoterMakerView.as_view(),name='voter_gen'),
]