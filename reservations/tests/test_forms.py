from django.test import TestCase
from django.utils.timezone import now, timedelta
from reservations.forms import ReservationForm

class ReservationFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'first_name': 'john',
            'last_name': 'doe',
            'email': 'john.doe@example.com',
            'number_of_persons': 5,
            'date_booking': now() + timedelta(days=1),
            'time': '18:00'
        }

    def test_valid_form(self):
        """Test si le formulaire est valide avec des données correctes."""
        form = ReservationForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_number_of_persons_invalid(self):
        """Test si le formulaire renvoie une erreur pour un nombre de personnes invalide."""
        invalid_data = self.valid_data.copy()
        invalid_data['number_of_persons'] = 0  # Nombre invalide
        form = ReservationForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('number_of_persons', form.errors)
        self.assertEqual(
            form.errors['number_of_persons'][0],
            "The number of persons must be greater than 0."
        )

    def test_date_booking_in_past(self):
        """Test si le formulaire renvoie une erreur pour une date dans le passé."""
        invalid_data = self.valid_data.copy()
        invalid_data['date_booking'] = now() - timedelta(days=1)  # Date dans le passé
        form = ReservationForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date_booking', form.errors)
        self.assertEqual(
            form.errors['date_booking'][0],
            "The date cannot be in the past."
        )

    def test_date_booking_empty(self):
        """Test si le formulaire renvoie une erreur lorsque la date est vide."""
        invalid_data = self.valid_data.copy()
        invalid_data['date_booking'] = None  # Date vide
        form = ReservationForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date_booking', form.errors)
        self.assertEqual(
            form.errors['date_booking'][0],
            "The booking date cannot be empty."
        )