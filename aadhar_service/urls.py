from django.urls import path
from .views import *

urlpatterns = [
    path('find_aadhar/', AadharFindView.as_view(), name='find_aadhar'),
    path('pdf_aadhar/', AadharPdfView.as_view(), name='pdf_aadhar'),
    path('aadhar_list/', AadharFindRecordView.as_view(), name='aadhar_records'),
    path('pdf_aadhar_list/', AadharPdfRecordView.as_view(), name='aadhar_pdf_records'),
    path('aadhar_to_pdf/', AadharToPdfView.as_view(), name='aadhar_no_to_pdf'),
    path('aadhar_to_pdf_list/', AadharToPdfRecordView.as_view(), name='aadhar_no_to_pdf_records'),
]
