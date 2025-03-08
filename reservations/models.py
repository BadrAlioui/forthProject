from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    number_of_persons = models.IntegerField()
    date_booking = models.DateTimeField()
    
    class Meta:
        unique_together = ["last_name", "date_booking", "email"]

    def __str__(self):
        return f"You booked a table for {self.date_booking}"

    def clean(self):
        # Assurez-vous que les noms sont en minuscule pour éviter les doublons
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()

        # Vérifier les doublons en excluant l'instance actuelle
        if Reservation.objects.filter(
            first_name=self.first_name,
            last_name=self.last_name,
            date_booking=self.date_booking
        ).exclude(pk=self.pk).exists():
            raise ValidationError("You have already booked a table for this date!")

        # Vérifier que number_of_persons est défini et valide
        if self.number_of_persons is None:
            raise ValidationError("The number of persons is required.")

        if self.number_of_persons <= 0:
            raise ValidationError("The number of persons must be greater than 0.")

        # Calculer le total des réservations en excluant l'instance actuelle
        total_persons = Reservation.objects.filter(
            date_booking=self.date_booking
        ).exclude(pk=self.pk).aggregate(total=models.Sum('number_of_persons'))['total'] or 0

        # Vérifier la capacité maximale
        if total_persons + self.number_of_persons > 15:
            raise ValidationError("The restaurant is full for this date!")

        # Vérifier que la date de réservation est dans le futur
        if self.date_booking is None:
            raise ValidationError("The booking date cannot be empty.")
        if self.date_booking < now():
            raise ValidationError("The date cannot be in the past.")
