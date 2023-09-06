from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeView
from django.contrib.auth.views import LoginView
from accounts.views import ProfileView, WalletView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('wallet/', WalletView.as_view(), name='wallet'),
    path('auth/login/', LoginView.as_view(template_name="pages/login.html",
                                          redirect_authenticated_user=True), name='login'),
    path('auth/', include('rest_framework.urls')),

    # admin paths
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
