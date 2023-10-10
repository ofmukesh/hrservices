from pan_service.urls import urlpatterns as pan_service_patters
from dl_service.urls import urlpatterns as dl_service_patters
from voter_service.urls import urlpatterns as voter_service_patters
from aadhar_service.urls import urlpatterns as aadhar_service_patters
from covid_service.urls import urlpatterns as covid_service_patters
from aayushman_service.urls import urlpatterns as aayushman_service_patters

urlpatterns = pan_service_patters+dl_service_patters+voter_service_patters+aadhar_service_patters+covid_service_patters+aayushman_service_patters