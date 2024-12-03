from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def reservation_page(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(
        request, "reservations/reservations.html",
        context={'reservations': reservations}
    )


@login_required(login_url="/accounts/login/")
def liste_reservation(request):
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
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Filter reservations by first and last name
        reservations = Reservation.objects.filter(
            first_name=first_name, last_name=last_name, user=request.user
        )
        if reservations.exists():
            # you can either delete all or handle accordingly
            reservations.delete()  # Deletes all matching reservations
            messages.success(request, "Reservation(s) deleted successfully")
        else:
            messages.error(request, "No matching reservations found.")
        return redirect("reservations:liste")
    return redirect("reservations:liste")
