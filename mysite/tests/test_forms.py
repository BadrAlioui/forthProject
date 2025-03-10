"""
This module contains tests for the ContactForm.
It uses Django's TestCase to ensure
that the contact form behaves as expected when submitted.
"""

from django.test import TestCase
from django.urls import reverse
from mysite.forms import ContactForm


class TestContactForm(TestCase):
    """
    Tests for the ContactForm submission process.
    """

    def test_create_contact_form_when_submitting(self):
        """
        Test that submitting the contact form with
        valid data redirects as expected.
        This test simulates a POST request to the
        'contact' URL with valid form data.
        It then checks that the response status
        code is 302 (redirect) and that the
        redirection is to the contact page.
        """
        form_data = {
            'name': 'testuser',
            'email': 'test@test.com',
            'message': 'Hello, this is a test message'
        }
        response = self.client.post(reverse('contact'), data=form_data)

        # Check that the form submission resulted in a redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact'))
