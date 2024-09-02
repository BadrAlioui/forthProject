from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages





def reservation_page(request):
    reservations = Reservation.objects.all()
    return  render(request, "reservations/reservations.html", context={'reservations':reservations})

def create_reservation(request):
    if request.method == "POST":
        form = ReservationForm
        if form.is_valid():
            form.save()
            
            messages.success(request, ('Reservation has been added'))
            return redirect('home')
        else:
            messages.success(request, ('there is an error'))
            return render(request, "reservations/create_reservations.html", {})
    else:
        return render(request, "reservations/create_reservations.html", {})
    

        

    
