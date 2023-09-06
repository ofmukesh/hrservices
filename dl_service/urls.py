from django.urls import path
from .views import DlFindView, DlPdfView, DlFindRecordView, DlPdfRecordView

urlpatterns = [
    path('find_dl/', DlFindView.as_view(), name='find_dl'),
    path('pdf_dl/', DlPdfView.as_view(), name='pdf_dl'),
    path('dl_list/', DlFindRecordView.as_view(), name='dl_records'),
    path('pdf_dl_list/', DlPdfRecordView.as_view(), name='dl_pdf_records'),
]
