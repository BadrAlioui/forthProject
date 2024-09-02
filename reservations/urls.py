

from django.urls import path

from . import views

app_name ="reservations"

urlpatterns = [
    
    
    path('', views.reservation_page, name="reservations"),
    path('create/', views.create_reservation, name="create")
    

]