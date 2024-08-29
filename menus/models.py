from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_displayed = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png')


    def __str__(self):
        return self.title



