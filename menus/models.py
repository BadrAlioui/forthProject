from django.db import models
#https://www.youtube.com/watch?v=nwwuynnCYE0
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

class Menu(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.1)])
    date_displayed = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default="images/default.png")


    def __str__(self):
        return self.title