"""
This module contains the form for creating or updating menu items.
It uses Django's ModelForm to automatically generate form fields based on the Menu model.
"""

from django.forms import ModelForm
from .models import Menu

class MenuForm(ModelForm):
    """
    A form for creating or updating a Menu item.

    This form includes fields for title, content, slug, price, and image,
    corresponding to the Menu model. It helps with validating and saving
    data related to menu items.
    """
    class Meta:
        model = Menu
        fields = ['title', 'content', 'slug', 'price', 'image']
