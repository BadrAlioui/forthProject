from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import re_path
from django.views.static import serve



def reservation_page(request):
    reservations = Reservation.objects.all()
    return render(request, "reservations/reservations.html", context={'reservations':reservations})


def liste_reservation(request):
    
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking has been added")
            return redirect('home')  # Redirect back to the home page
        else:
            messages.error(request, "There was an error in your submission or the reservation already exists.")
    else:
        form = ReservationForm()  # If it's a GET request, instantiate a blank form
    
    reservations = Reservation.objects.all()  # Fetch all reservations

    return render(request, "reservations/liste_reservation.html", {
        "form": form,
        "reservations": reservations  # Pass reservations to the template
    })

@login_required(login_url="/accounts/login/")
def edit(request, list_id):
    # Obtain the reservation to be edited
    get_reservation = get_object_or_404(Reservation, pk=list_id)
    
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=get_reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking has been edited")
            return redirect('reservations:liste')  # lead to the list of reservations after editing
        else:
            messages.error(request, "There was an error in your submission or the reservation already exists.")
    else:
        form = ReservationForm(instance=get_reservation)
    
    return render(request, "reservations/edit_reservation.html", {
        "get_reservation": get_reservation,
        "form": form
    })

@login_required(login_url="/accounts/login/")
def delete_reservation(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        # research reservation
        reservation = get_object_or_404(Reservation, first_name=first_name, last_name=last_name)
        
        # delelte reservation
        reservation.delete()
        messages.success(request, "Reservation deleted successfully")
        return redirect("reservations:liste")  # lead to the list of reservations
    return redirect("reservations:liste")  # lead to the list of reservations




        

    