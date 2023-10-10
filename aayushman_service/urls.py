from django.urls import path
from .views import *

urlpatterns = [
    path('pdf_aayushman/', AayushmanPdfView.as_view(), name='pdf_aayushman'),
    path('pdf_aayushman_list/', AayushmanPdfRecordView.as_view(), name='aayushman_pdf_records'),
]
