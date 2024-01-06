from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeView
from django.contrib.auth.views import LoginView
from accounts.views import ProfileView, WalletView, UserTransactionsHistoryView, signup

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('services/', include('services.urls')),
    path('wallet/', WalletView.as_view(), name='wallet'),
    path('transactions/', UserTransactionsHistoryView.as_view(), name='transactions'),
    path('auth/login/', LoginView.as_view(template_name="pages/login.html",
                                          redirect_authenticated_user=True), name='login'),
    path('auth/signup/', signup, name='signup'),
    path('auth/', include('rest_framework.urls')),

    # admin paths
    path('marco7/', admin.site.urls),
    path('marco7_services/', include("admin_services.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
