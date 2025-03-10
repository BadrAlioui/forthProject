"""
This module tests the Menu form functionality.
It checks that the form works as expected with valid data,
and that it properly handles missing data by showing errors.
"""

import os
from django.test import TestCase
from django.urls import reverse
from menus.models import Menu
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

# Get the directory of the current file (menus/tests)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up two levels to reach the project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(CURRENT_DIR))
# Construct the relative path to your test image file in media
image_path = os.path.join(PROJECT_ROOT, 'media', 'couscous.jpg')

with open(image_path, 'rb') as img:
    image = SimpleUploadedFile(
        name='couscous.jpg',
        content=img.read(),
        content_type='image/jpeg'
    )


class MenuFormTest(TestCase):
    """
    This TestCase checks the behavior of the Menu form.
    It ensures that the form creates a new Menu when provided with valid data,
    and that it shows the proper error messages when required
    fields are missing.
    """

    def test_menu_form_valid_data(self):
        """
        Test that submitting the Menu form with valid data creates a new Menu
        and redirects the user (HTTP status 302).
        """
        form_data = {
            'title': 'Menu Test',
            'content': 'Example for the test.',
            'slug': 'menu-test',
            'price': 10.00,
            'image': image,
        }
        admin_user = User.objects.create_superuser(username='admin',
                                                   password='admin123')
        self.client.login(username='admin', password='admin123')
        response = self.client.post(reverse('menus:create'), data=form_data)

        # Verify that the response is a redirect and that the Menu was created.
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Menu.objects.filter(title='Menu Test').exists())

    def test_menu_form_no_data(self):
        """
        Test that submitting the Menu form without any data
        returns the form with errors,
        and no Menu instance is created.
        """
        # Create an admin user and log in.
        admin_user = User.objects.create_superuser(username='admin',
                                                   password='admin123')
        self.client.login(username='admin', password='admin123')

        # Submit an empty form.
        response = self.client.post(reverse('menus:create'), data={})

        # Check that the form is re-rendered with a status of 200.
        self.assertEqual(response.status_code, 200)

        # Ensure the context contains the form and that it has errors.
        self.assertTrue('form' in response.context)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('slug', form.errors)
        self.assertIn('price', form.errors)

        # Confirm that no new Menu was created.
        self.assertFalse(Menu.objects.exists())
