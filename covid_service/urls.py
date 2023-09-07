from django.urls import path
from .views import CovidView, CovidRecordView

urlpatterns = [
    path('covid/', CovidView.as_view(), name='covid'),
    path('covid_list/', CovidRecordView.as_view(), name='covid_records'),
]
