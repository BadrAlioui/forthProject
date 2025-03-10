from django.urls import path

from . import views

app_name = "reservations"

urlpatterns = [
    path('', views.reservation_page, name="reservations"),
    path('liste/', views.liste_reservation, name="liste"),
    path('edit/<list_id>', views.edit, name="edit"),
    path('delete/<int:list_id>', views.delete_reservation, name="delete"),
]