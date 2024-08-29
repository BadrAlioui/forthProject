from django.contrib import admin
from django.urls import path

from . import views

app_name = "menus"

urlpatterns = [
    
    path('', views.menus_page, name='menus'),
    path('create/', views.create_menu, name="create" ),
    path('<slug:slug>/', views.menu_page, name="menu")
    
]