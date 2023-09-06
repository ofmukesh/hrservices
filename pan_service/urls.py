from django.urls import path
from .views import NsdlPanFindView,PanPdfView

urlpatterns = [
    path('nsdl_pan/', NsdlPanFindView.as_view(),name='find_nsdl_pan'),
    path('pdf_pan/', PanPdfView.as_view(),name='pdf_pan'),
]