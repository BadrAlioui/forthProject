from django.shortcuts import render, redirect, get_object_or_404
from reservations.models import Reservation
from reservations.forms import ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def reservation_page(request):
    """Affiche la page de création de réservation et les réservations existantes."""
    reservations = Reservation.objects.filter(user=request.user)
    if not reservations.exists():
        messages.info(request, "You have no reservations.")
    return render(
        request, "reservations/reservations.html",
        context={"reservations": reservations}
    )


@login_required(login_url="/accounts/login/")
def liste_reservation(request):
    """Affiche la liste des réservations et permet d'en ajouter."""
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Booking has been added")
            return redirect("home")
        else:
            for _, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = ReservationForm()

    reservations = Reservation.objects.filter(user=request.user)
    if not reservations.exists():
        messages.info(request, "No reservations found.")
    
    return render(
        request, "reservations/liste_reservation.html",
        context={
            "form": form,
            "reservations": reservations
        }
    )


@login_required(login_url="/accounts/login/")
def edit(request, list_id):
    """Affiche et permet de modifier une réservation existante."""
    try:
        get_reservation = Reservation.objects.get(pk=list_id)
    except Reservation.DoesNotExist:
        messages.error(request, "Reservation not found.")
        return redirect("reservations:liste")

    if get_reservation.user != request.user:
        messages.error(request, "Not allowed to edit this reservation.")
        return redirect("reservations:liste")

    if request.method == "POST":
        form = ReservationForm(request.POST, instance=get_reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking has been edited")
            return redirect("reservations:liste")
        else:
            # Log des erreurs pour debug si nécessaire
            print("Form errors:", form.errors)
            messages.error(request, "There was an error in your submission.")
    else:
        form = ReservationForm(instance=get_reservation)

    return render(
        request, "reservations/edit_reservation.html",
        context={
            "get_reservation": get_reservation,
            "form": form
        }
    )


@login_required(login_url="/accounts/login/")
def delete_reservation(request):
    """Permet de supprimer une réservation existante."""
    if request.method == "POST":
        reservation_id = request.POST.get("reservation_id")  # Modification pour utiliser l'ID
        try:
            reservation = Reservation.objects.get(id=reservation_id, user=request.user)
            reservation.delete()
            messages.success(request, "Reservation deleted successfully.")
        except Reservation.DoesNotExist:
            messages.error(request, "Reservation not found.")
        
        return redirect("reservations:liste")

    return redirect("reservations:liste")