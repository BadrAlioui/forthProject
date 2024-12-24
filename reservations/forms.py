from django import forms
from .models import Reservation
from django.utils.timezone import now


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['user']
    date_booking = forms.DateTimeField(required=False)

    def clean_number_of_persons(self):
        number_of_persons = self.cleaned_data.get('number_of_persons')
        if number_of_persons is None or number_of_persons <= 0:
            raise forms.ValidationError(
                "The number of persons must be greater than 0."
                )
        return number_of_persons

    def clean_date_booking(self):
        date_booking = self.cleaned_data.get('date_booking')
        if date_booking is None:
            raise forms.ValidationError("The booking date cannot be empty.")
        if date_booking < now():
            raise forms.ValidationError("The date cannot be in the past.")
        return date_booking
