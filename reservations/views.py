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
def delete_reservation(request, list_id):
    """
    Delete a specific reservation.

    This view handles the deletion of a reservation identified by its primary key (list_id).
    It ensures that the reservation belongs to the currently logged-in user. For GET requests,
    it renders a confirmation template asking the user to confirm deletion. For POST requests,
    it deletes the reservation, shows a success message, and redirects the user to the reservations list.

    Args:
        request: The HTTP request object.
        list_id (int): The primary key of the reservation to be deleted.

    Returns:
        An HTTP redirect response upon successful deletion, or an HTTP response rendering the
        deletion confirmation template if the request method is GET.
    """
    reservation = get_object_or_404(Reservation, pk=list_id, user=request.user)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Reservation deleted successfully")
        return redirect("reservations:liste")
    return render(request, "reservations/delete_confirmation.html", {"reservation": reservation})


