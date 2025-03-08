"""
This module defines the Menu model for our restaurant application.
It represents a menu item with details such as its title, description, slug, price,
display date, and an associated image.
"""

from django.db import models
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

class Menu(models.Model):
    """
    Represents a menu item in the restaurant.

    Attributes:
        title (str): The name of the menu item.
        content (str): A description of the menu item (optional).
        slug (str): A unique slug for the menu item, used in URLs.
        price (Decimal): The price of the menu item. Must be at least 0.1.
        date_displayed (datetime): The timestamp when the menu item was added.
        image (CloudinaryField): The image associated with the menu item.
    """
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.1)])
    date_displayed = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')

    def __str__(self):
        """
        Return a human-friendly string representation of the menu item.
        """
        return self.title
