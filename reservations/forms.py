from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    date_booking = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Reservation
        exclude = ['user']
        
