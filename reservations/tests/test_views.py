from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from reservations.models import Reservation
from django.utils.timezone import now, timedelta


class ReservationViewsTest(TestCase):
    def setUp(self):
        """Initialise a user and a reservation for the tests."""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.reservation = Reservation.objects.create(
            user=self.user,
            first_name="john",
            last_name="doe",
            email="john.doe@example.com",
            number_of_persons=5,
            date_booking=now() + timedelta(days=1),
            time="18:00"
        )

    def test_reservation_page(self):
        """Test if the reservations view displays the reservations."""
        response = self.client.get(reverse("reservations:reservations"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reservations/reservations.html")
        self.assertContains(response, "john".lower())

    def test_liste_reservation_get(self):
        """Test if the list view displays the reservations."""
        response = self.client.get(reverse("reservations:liste"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reservations/liste_reservation.html")
        self.assertContains(response, "john".lower())

    def test_liste_reservation_post_valid(self):
        """Test if a new reservation can be created."""
        response = self.client.post(
            reverse("reservations:liste"),
            data={
                "first_name": "alice",
                "last_name": "smith",
                "email": "alice.smith@example.com",
                "number_of_persons": 2,
                "date_booking": now() + timedelta(days=2),
                "time": "19:00"
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Reservation.objects.filter(first_name="alice", last_name="smith").exists()
        )

    def test_edit_reservation_get(self):
        """Test if an existing reservation can be edited."""
        response = self.client.get(reverse("reservations:edit", args=[self.reservation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reservations/edit_reservation.html")
        self.assertContains(response, "john".lower())

    def test_edit_reservation_post_valid(self):
        """Test if an existing reservation can be edited."""
        response = self.client.post(
            reverse("reservations:edit", args=[self.reservation.id]),
            data={
                "first_name": "john",
                "last_name": "doe",
                "email": "john.doe@example.com",
                "number_of_persons": 10,
                "date_booking": now() + timedelta(days=1),
                "time": "18:30"
            }
        )
        self.assertEqual(response.status_code, 302)
        self.reservation.refresh_from_db()
        self.assertEqual(self.reservation.number_of_persons, 10)

    def test_delete_reservation_post(self):
        """Test if an existing reservation can be deleted."""
        response = self.client.post(
            reverse("reservations:delete"),
            data={"first_name": "john", "last_name": "doe"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Reservation.objects.filter(pk=self.reservation.pk).exists()
        )

    def test_access_without_login(self):
        """Test if the user is redirected to the login page if not authenticated."""
        self.client.logout()
        response = self.client.get(reverse("reservations:reservations"))    
        self.assertRedirects(response, "/accounts/login/?next=/reservations/")