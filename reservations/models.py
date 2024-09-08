from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_persons = models.PositiveIntegerField()
    date_booking = models.DateTimeField()
    time = models.TimeField(default='00:00')

    class Meta:
        unique_together = ["first_name", "last_name", "date_booking"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} has booked a table for {self.date_booking}"

    def clean(self):
        super().clean()
        if self.date_booking < timezone.now():
            raise ValidationError("The date cannot be in the past!")
        if Reservation.objects.filter(date_booking=self.date_booking).count() >= 15:
            raise ValidationError("The restaurant is full for this date!")
        if Reservation.objects.filter(first_name=self.first_name, last_name=self.last_name, date_booking=self.date_booking).exists():
            raise ValidationError("You have already booked a table for this date!")