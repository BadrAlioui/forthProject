
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('contact/', views.contact_page, name='contact'),
    path('menus/', include('menus.urls')),
    # path('reservations/', include('reservations.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)