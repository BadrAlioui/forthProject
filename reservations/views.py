from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages

def reservation_page(request):
    reservations = Reservation.objects.all()
    return render(request, "reservations/reservations.html", context={'reservations':reservations})


def liste_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking has been added")
            return redirect('reservations:liste')  # Redirect back to the same page to see the updated list
        else:
            messages.error(request, "There was an error in your submission.")
    else:
        form = ReservationForm()  # If it's a GET request, instantiate a blank form
    
    reservations = Reservation.objects.all()  # Fetch all reservations

    return render(request, "reservations/liste_reservation.html", {
        "form": form,
        "reservations": reservations  # Pass reservations to the template
    })
        

    
