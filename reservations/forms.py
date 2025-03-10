"""
This module defines the ReservationForm used to create or update a reservation.
It is linked to the Reservation model and customizes the input for
the booking date and time.
"""


from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    """
    A ModelForm for the Reservation model.
    This form customizes the 'date_booking' field to use
    an HTML5 datetime-local input,
    which allows users to easily select both a date and a time.
    The 'user' field is excluded
    because it is automatically set based on the logged-in user.
    """
    date_booking = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        error_messages={'required': "The booking date cannot be empty."}
    )

    class Meta:
        model = Reservation
        exclude = ['user']
