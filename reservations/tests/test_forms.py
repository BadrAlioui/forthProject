"""
This module contains tests for the ReservationForm.
It verifies that the form validates data correctly and
rejects invalid input such as a past or empty booking date,
or an invalid number of persons.
"""

from django.test import TestCase
from django.utils.timezone import now, timedelta
from reservations.forms import ReservationForm

class ReservationFormTest(TestCase):
    """
    Test cases for the ReservationForm.

    These tests check that:
      - The form is valid when provided with correct data.
      - An error is raised when the number of persons is not valid.
      - An error is raised when the booking date is in the past.
      - An error is raised when the booking date is empty.
    """

    def setUp(self):
        """
        Set up valid data for testing the ReservationForm.
        """
        self.valid_data = {
            'first_name': 'john',
            'last_name': 'doe',
            'email': 'john.doe@example.com',
            'number_of_persons': 5,
            'date_booking': now() + timedelta(days=1),
        }

    def test_valid_form(self):
        """
        Test that the form is valid when given correct data.
        """
        form = ReservationForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_number_of_persons_invalid(self):
        """
        Test that the form returns an error when the number of persons is invalid.
        """
        invalid_data = self.valid_data.copy()
        invalid_data['number_of_persons'] = 0  # Invalid number
        form = ReservationForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('number_of_persons', form.errors)
        self.assertEqual(
            form.errors['number_of_persons'][0],
            "The number of persons must be greater than 0."
        )

    def test_date_booking_in_past(self):
        """
        Test that the form returns an error when the booking date is in the past.
        """
        invalid_data = self.valid_data.copy()
        invalid_data['date_booking'] = now() - timedelta(days=1)  # Date in the past
        form = ReservationForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date_booking', form.errors)
        self.assertEqual(
            form.errors['date_booking'][0],
            "The date cannot be in the past."
        )

    def test_date_booking_empty(self):
        """
        Test that the form returns an error when the booking date is empty.
        """
        invalid_data = self.valid_data.copy()
        invalid_data['date_booking'] = None  # Empty date
        form = ReservationForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date_booking', form.errors)
        self.assertEqual(
            form.errors['date_booking'][0],
            "The booking date cannot be empty."
        )
