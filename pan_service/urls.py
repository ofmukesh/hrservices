from django.urls import path
from .views import NsdlPanFindView,PanPdfView,NsdlPanFindRecordView,PanPdfRecordView

urlpatterns = [
    path('pan/', NsdlPanFindView.as_view(),name='find_pan'),
    path('pdf_pan/', PanPdfView.as_view(),name='pdf_pan'),
    path('pan_list/', NsdlPanFindRecordView.as_view(),name='pan_records'),
    path('pdf_pan_list/', PanPdfRecordView.as_view(),name='pan_pdf_records'),
]