from django.db import models

class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_persons = models.PositiveIntegerField()
    date_booking = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} has booked a table for {self.date_booking}"
