"""
This module contains the views for managing reservations.
Users can view, add, edit, and delete their reservations.
Each view requires the user to be logged in.
"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def reservation_page(request):
    """
    Display the reservations of the logged-in user.
    Retrieves all reservations associated with the current user and renders
    them using the 'reservations/reservations.html' template.
    """
    reservations = Reservation.objects.filter(user=request.user)
    return render(
        request, "reservations/reservations.html",
        context={'reservations': reservations}
    )


@login_required(login_url="/accounts/login/")
def liste_reservation(request):
    """
    Handle reservation creation and display the list of reservations.
    If the request is a POST, it validates and saves the reservation form,
    associating it with the current user.
    It also shows success or error messages.
    If the request is a GET,
    it displays an empty form along with the list of existing
    reservations for the current user.
    """
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Booking has been added")
            return redirect('home')
        else:
            for _, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = ReservationForm()

    reservations = Reservation.objects.filter(user=request.user)

    return render(
        request, "reservations/liste_reservation.html", {
            "form": form,
            "reservations": reservations
        }
    )


@login_required(login_url="/accounts/login/")
def edit(request, list_id):
    """
    Edit an existing reservation.
    Retrieves the reservation using the provided list_id.
    Only allows the owner of the reservation to edit it.
    If the reservation is found and belongs to the user, it processes
    the form submission to update the reservation; otherwise,
    it shows an error message.
    """
    try:
        get_reservation = Reservation.objects.get(pk=list_id)
    except Reservation.DoesNotExist:
        messages.error(request, "Reservation not found.")
        return redirect('reservations:liste')

    if get_reservation.user != request.user:
        messages.error(request, "Not allowed to edit this reservation.")
        return redirect('reservations:liste')

    if request.method == "POST":
        form = ReservationForm(request.POST, instance=get_reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking has been edited")
            return redirect('reservations:liste')
        else:
            print(form.errors)
            messages.error(request, "There was an error in your submission.")
    else:
        form = ReservationForm(instance=get_reservation)

    return render(
        request, "reservations/edit_reservation.html", {
            "get_reservation": get_reservation,
            "form": form
        }
    )


@login_required(login_url="/accounts/login/")
def delete_reservation(request):
    """
    Delete one or more reservations based on first and last name.
    If the request is POST,
    it retrieves the first_name and last_name from the POST data,
    filters the reservations for the current user, and deletes them if found.
    Displays appropriate success or error messages and
    then redirects to the reservations list.
    """
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Filter reservations by first and last name for the current user.
        reservations = Reservation.objects.filter(
            first_name=first_name, last_name=last_name, user=request.user
        )
        if reservations.exists():
            reservations.delete()  # Deletes all matching reservations.
            messages.success(request, "Reservation(s) deleted successfully")
        else:
            messages.error(request, "No matching reservations found.")
        return redirect("reservations:liste")
    return redirect("reservations:liste")
