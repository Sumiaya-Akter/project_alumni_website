from django.contrib import admin
from django.urls import path, include
from login import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('', views.home, name='home'),
    path('LOGIN', views.LOGIN, name='LOGIN'),
    path('logout', views.logout_view, name='logout'),
    path('Donor_Sponsor', views.Donor_Sponsor, name="login-Donor_Sponsor"),
    path('contact_us', views.contact_us, name="login-contact_us"),
    path('membership', views.membership, name="membership"),
    path('Events', views.Events, name="login-Events")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
