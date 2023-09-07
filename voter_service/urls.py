from django.urls import path
from .views import VoterPdfView, VoterPdfRecordView

urlpatterns = [
    path('pdf_voter/', VoterPdfView.as_view(), name='pdf_voter'),
    path('pdf_voter_list/', VoterPdfRecordView.as_view(), name='voter_pdf_records'),
]
