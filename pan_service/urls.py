from django.urls import path
from .views import *

urlpatterns = [
    path('pan/', NsdlPanFindView.as_view(),name='find_pan'),
    path('pdf_pan/', PanPdfView.as_view(),name='pdf_pan'),
    path('pan_list/', NsdlPanFindRecordView.as_view(),name='pan_records'),
    path('pdf_pan_list/', PanPdfRecordView.as_view(),name='pan_pdf_records'),
    path('uti_pan_pdf/', UtiPanPdfView.as_view(),name='uti_pan_pdf'),
    path('uti_records/', UtiPanPdfRecordView.as_view(),name='uti_pan_pdf_records'),
    path('instant_pan/', InstantPanFindView.as_view(),name='instant_find_pan'),
    path('instant_pan_records/', InstantPanRecordView.as_view(),name='instant_pan_record'),
]