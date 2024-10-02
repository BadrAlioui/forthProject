from django import forms
from .models import Reservation
from django.utils import timezone



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        

    
