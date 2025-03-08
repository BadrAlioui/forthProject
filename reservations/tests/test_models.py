"""
This module contains tests for the Reservation model.
It verifies that the Reservation model behaves as expected, including:
- Successful creation of a reservation.
- Validation errors for invalid number of persons.
- Prevention of duplicate bookings on the same day.
- Enforcement of the restaurant's maximum capacity.
"""

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from reservations.models import Reservation
from django.utils.timezone import now, timedelta

class ReservationModelTest(TestCase):
    """
    Test cases for the Reservation model.
    """

    def setUp(self):
        """
        Set up a test user and a default booking date for tomorrow.
        """
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.date_booking = now() + timedelta(days=1)  # Reservation for tomorrow

    def test_reservation_creation(self):
        """
        Test that a valid reservation is created successfully and that its string
        representation is correct.
        """
        reservation = Reservation.objects.create(
            user=self.user,
            first_name="john",
            last_name="doe",
            email="john.doe@example.com",
            number_of_persons=5,
            date_booking=self.date_booking,
        )
        self.assertEqual(str(reservation), f"You booked a table for {reservation.date_booking}")

    def test_number_of_persons_validation(self):
        """
        Test that a reservation with an invalid number of persons (<= 0)
        raises a ValidationError.
        """
        reservation = Reservation(
            user=self.user,
            first_name="jane",
            last_name="doe",
            email="jane.doe@example.com",
            number_of_persons=0,  # Invalid number
            date_booking=self.date_booking,
        )
        with self.assertRaises(ValidationError):
            reservation.full_clean()

    def test_duplicate_booking(self):
        """
        Test that creating a duplicate reservation for the same day
        raises a ValidationError.
        """
        Reservation.objects.create(
            user=self.user,
            first_name="john",
            last_name="doe",
            email="john.doe@example.com",
            number_of_persons=3,
            date_booking=self.date_booking,
        )
        duplicate_reservation = Reservation(
            user=self.user,
            first_name="john",
            last_name="doe",
            email="john.doe@example.com",
            number_of_persons=2,
            date_booking=self.date_booking,
        )
        with self.assertRaises(ValidationError):
            duplicate_reservation.full_clean()

    def test_maximum_capacity(self):
        """
        Test that exceeding the restaurant's maximum capacity for a given booking
        date raises a ValidationError.
        """
        Reservation.objects.create(
            user=self.user,
            first_name="alice",
            last_name="smith",
            email="alice.smith@example.com",
            number_of_persons=10,
            date_booking=self.date_booking,
        )
        over_capacity_reservation = Reservation(
            user=self.user,
            first_name="bob",
            last_name="johnson",
            email="bob.johnson@example.com",
            number_of_persons=6,  # This will exceed the capacity of 15
            date_booking=self.date_booking,
        )
        with self.assertRaises(ValidationError):
            over_capacity_reservation.full_clean()
