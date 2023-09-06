from pan_service.urls import urlpatterns as pan_service_patters
from dl_service.urls import urlpatterns as dl_service_patters

urlpatterns = pan_service_patters+dl_service_patters
