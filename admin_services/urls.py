from django.urls import path
from pan_service.views import AadharToPanView
from .views import AdminView,VoterMakerView

urlpatterns = [
    path('', AdminView.as_view(),name='home_admin'),
    path('aadhar_to_pan/', AadharToPanView.as_view(),name='aadhar_to_pan'),
    path('voter_gen/', VoterMakerView.as_view(),name='voter_gen'),
]