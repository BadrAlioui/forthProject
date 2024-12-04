from django.test import TestCase
from reservations.models import Reservation
from django.utils.timezone import now

class ReservationTestCase(TestCase):
    def test_create_reservation(self):
        Reservation.objects.create(
            first_name="John",
            last_name="Doe",
            email="test@example.com",
            number_of_persons=4,
            date_booking=now(),

        )
        self.assertEqual(Reservation.objects.count(), 1)
        self.assertEqual(Reservation.objects.get().first_name, "john")
        self.assertEqual(Reservation.objects.get().last_name, "doe")
        self.assertEqual(Reservation.objects.get().email, "test@example.com")
            