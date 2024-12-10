from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from reservations.models import Reservation
from django.utils.timezone import now, timedelta

class ReservationModelTest(TestCase):
    def setUp(self):
        # Créer un utilisateur pour les tests
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.date_booking = now() + timedelta(days=1)  # Réservation pour demain

    def test_reservation_creation(self):
        # Tester la création valide d'une réservation
        reservation = Reservation.objects.create(
            user=self.user,
            first_name="john",
            last_name="doe",
            email="john.doe@example.com",
            number_of_persons=5,
            date_booking=self.date_booking,
            time="18:00"
        )
        self.assertEqual(str(reservation), f"You booked a table for {reservation.date_booking}")

    def test_number_of_persons_validation(self):
        # Tester le cas où number_of_persons est invalide
        reservation = Reservation(
            user=self.user,
            first_name="jane",
            last_name="doe",
            email="jane.doe@example.com",
            number_of_persons=0,  # Nombre invalide
            date_booking=self.date_booking,
            time="18:00"
        )
        with self.assertRaises(ValidationError):
            reservation.full_clean()

    def test_duplicate_booking(self):
        # Tester les doublons
        Reservation.objects.create(
            user=self.user,
            first_name="john",
            last_name="doe",
            email="john.doe@example.com",
            number_of_persons=3,
            date_booking=self.date_booking,
            time="18:00"
        )
        duplicate_reservation = Reservation(
            user=self.user,
            first_name="john",
            last_name="doe",
            email="john.doe@example.com",
            number_of_persons=2,
            date_booking=self.date_booking,
            time="18:00"
        )
        with self.assertRaises(ValidationError):
            duplicate_reservation.full_clean()

    def test_maximum_capacity(self):
        # Tester la capacité maximale
        Reservation.objects.create(
            user=self.user,
            first_name="alice",
            last_name="smith",
            email="alice.smith@example.com",
            number_of_persons=10,
            date_booking=self.date_booking,
            time="18:00"
        )
        over_capacity_reservation = Reservation(
            user=self.user,
            first_name="bob",
            last_name="johnson",
            email="bob.johnson@example.com",
            number_of_persons=6,
            date_booking=self.date_booking,
            time="18:00"
        )
        with self.assertRaises(ValidationError):
            over_capacity_reservation.full_clean()