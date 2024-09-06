from django.apps import AppConfig
from django.contrib import admin

from .models import Menu

admin.site.register(Menu)


class MenusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menus'

