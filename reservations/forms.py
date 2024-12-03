from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['user']

    def clean_number_of_persons(self):
        number_of_persons = self.cleaned_data.get('number_of_persons')
        if number_of_persons is None or number_of_persons <= 0:
            raise forms.ValidationError("The number of persons must be greater than 0.")
        return number_of_persons

    def clean_date_booking(self):
        date_booking = self.cleaned_data.get('date_booking')
        if date_booking is None:
            raise ValidationError("The booking date cannot be empty.")
        if date_booking < now():
            raise ValidationError("The date cannot be in the past.")
        return date_booking

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        date_booking = cleaned_data.get('date_booking')

        # Vérification des réservations doublons
        if first_name and last_name and date_booking:
            if Reservation.objects.filter(
                first_name=first_name.lower(),
                last_name=last_name.lower(),
                date_booking=date_booking
            ).exists():
                raise forms.ValidationError("You have already booked a table for this date!")

        # Vérification de la limite des réservations
        if date_booking and Reservation.objects.filter(date_booking=date_booking).count() >= 15:
            raise forms.ValidationError("The restaurant is fully booked for this date and time.")

        return cleaned_data
