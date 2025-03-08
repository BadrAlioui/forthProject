"""
This module defines the Reservation model for our restaurant booking system.
It includes custom validation to ensure that users do not book more than one table
on the same day and that all reservation details meet our requirements.
"""

from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Reservation(models.Model):
    """
    Represents a table reservation at the restaurant.

    Attributes:
        user (User): The user who made the reservation (optional).
        first_name (str): The first name of the person booking.
        last_name (str): The last name of the person booking.
        email (str): The email address of the person booking.
        number_of_persons (int): The number of people included in the reservation.
        date_booking (datetime): The date and time of the reservation.
    
    The unique_together constraint ensures that the same person (identified by last_name and email)
    cannot book more than one reservation on the same day.
    """
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
        """Return a simple string representation of the reservation."""
        return f"You booked a table for {self.date_booking}"

    def clean(self):
        """
        Clean and validate the Reservation instance.

        This method normalizes the name and email fields to avoid issues with case or extra spaces.
        It then checks:
            - That the user hasn't already booked a table on the same day.
            - That the number of persons is defined and greater than zero.
            - That the total number of persons for the booking does not exceed the restaurant capacity.
            - That the booking date is not empty and is set in the future.

        Raises:
            ValidationError: If any validation fails.
        """
        # Normalize fields to avoid differences due to case or extra spaces.
        self.first_name = self.first_name.strip().lower()
        self.last_name = self.last_name.strip().lower()
        self.email = self.email.strip().lower()

        # Convert date_booking to a simple date (ignoring time).
        booking_date = self.date_booking.date() if self.date_booking else None

        # Check for duplicates by comparing only the date.
        if booking_date and Reservation.objects.filter(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            date_booking__date=booking_date  
        ).exclude(pk=self.pk).exists():
            raise ValidationError("You have already booked a table for this day!")

        # Check that number_of_persons is defined and valid.
        if self.number_of_persons is None:
            raise ValidationError("The number of persons is required.")
        if self.number_of_persons <= 0:
            raise ValidationError({'number_of_persons': "The number of persons must be greater than 0."})


        # Calculate the total persons already booked for this date.
        total_persons = Reservation.objects.filter(
            date_booking=self.date_booking
        ).exclude(pk=self.pk).aggregate(total=models.Sum('number_of_persons'))['total'] or 0

        # Check that the restaurant capacity is not exceeded.
        if total_persons + self.number_of_persons > 15:
            raise ValidationError("The restaurant is full for this date!")

        # Check that the booking date is provided and is in the future.
        if self.date_booking is None:
            raise ValidationError("The booking date cannot be empty.")
        if self.date_booking < now():
            raise ValidationError({'date_booking': "The date cannot be in the past."})

