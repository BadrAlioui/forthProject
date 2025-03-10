"""
This module contains tests for the home and contact pages.
It verifies that these pages load successfully and use the correct templates.
"""

from django.test import TestCase, SimpleTestCase


class TestHomePage(TestCase):
    """
    Test cases for verifying the home and contact page views.
    """

    def test_home_page(self):
        """
        Ensure that the home page loads successfully
        and uses 'home.html' as its template.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_contact_page(self):
        """
        Ensure that the contact page loads successfully
        and uses 'contact.html' as its template.
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
