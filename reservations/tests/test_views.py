"""
This module contains tests for the reservation views.
It checks that the reservation pages work as expected for creating,
editing, listing, deleting reservations, and that authentication is enforced.
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from reservations.models import Reservation
from django.utils.timezone import now, timedelta


class ReservationViewsTest(TestCase):
    """
    Test cases for reservation-related views.
    These tests verify that:
      - The reservations page displays the user's reservations.
      - The list view shows the correct reservation details.
      - New reservations can be created via POST requests.
      - Existing reservations can be edited and updated.
      - Reservations can be deleted.
      - Unauthenticated users are redirected to the login page.
    """

    def setUp(self):
        """
        Set up a test user and a sample reservation for the tests.
        The reservation is scheduled for tomorrow.
        """
        self.user = User.objects.create_user(username="testuser",
                                             password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.reservation = Reservation.objects.create(
            user=self.user,
            first_name="john",
            last_name="doe",
            email="john.doe@example.com",
            number_of_persons=5,
            date_booking=now() + timedelta(days=1),
        )

    def test_reservation_page(self):
        """
        Test if the reservations page displays the user's reservations.
        It should return status code 200 and use the correct template.
        """
        response = self.client.get(reverse("reservations:reservations"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reservations/reservations.html")
        self.assertContains(response, "john".lower())

    def test_liste_reservation_get(self):
        """
        Test if the list view displays the reservations.
        The view should render the appropriate
        template and show reservation details.
        """
        response = self.client.get(reverse("reservations:liste"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                "reservations/liste_reservation.html")
        self.assertContains(response, "john".lower())

    def test_liste_reservation_post_valid(self):
        """
        Test if a new reservation can be created via a POST request.
        After posting valid data, the view
        should redirect and the new reservation should exist.
        """
        response = self.client.post(
            reverse("reservations:liste"),
            data={
                "first_name": "alice",
                "last_name": "smith",
                "email": "alice.smith@example.com",
                "number_of_persons": 2,
                "date_booking": now() + timedelta(days=2),
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Reservation.objects.filter(first_name="alice",
                                       last_name="smith").exists()
        )

    def test_edit_reservation_get(self):
        """
        Test if the edit reservation view loads correctly.
        It should render the edit template and display
        the current reservation details.
        """
        response = self.client.get(reverse("reservations:edit",
                                           args=[self.reservation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reservations/edit_reservation.html")
        self.assertContains(response, "john".lower())

    def test_edit_reservation_post_valid(self):
        """
        Test if an existing reservation can be updated via a POST request.
        The reservation should be updated with the new data and
        the view should redirect.
        """
        response = self.client.post(
            reverse("reservations:edit", args=[self.reservation.id]),
            data={
                "first_name": "john",
                "last_name": "doe",
                "email": "john.doe@example.com",
                "number_of_persons": 10,
                "date_booking": now() + timedelta(days=1),
            }
        )
        self.assertEqual(response.status_code, 302)
        self.reservation.refresh_from_db()
        self.assertEqual(self.reservation.number_of_persons, 10)

    def test_delete_reservation_post(self):
        """
        Test if an existing reservation can be deleted via a POST request.
        After deletion, the reservation should no longer exist.
        """
        response = self.client.post(
            reverse("reservations:delete"),
            data={"first_name": "john", "last_name": "doe"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Reservation.objects.filter(pk=self.reservation.pk).exists()
        )

    def test_access_without_login(self):
        """
        Test that unauthenticated users are redirected to the login page.
        When not logged in, accessing the reservations page should
        redirect to login.
        """
        self.client.logout()
        response = self.client.get(reverse("reservations:reservations"))
        self.assertRedirects(response, "/accounts/login/?next=/reservations/")
