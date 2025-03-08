"""
This module tests the profile (menus) page view for authenticated users.
It ensures that logged-in users can access the page and that it displays
the expected menu items.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from menus.models import Menu

class TestProfilePage(TestCase):
    """
    Test case for the profile (menus) page view.

    This class verifies that an authenticated user can access the page and
    that it correctly displays menu items.
    """

    def test_profile_view_accessible_for_authenticated_user(self):
        """
        Test that the profile view is accessible for authenticated users and
        displays the expected menu.

        Steps:
            - Create a test user and log in.
            - Create a sample Menu object.
            - Access the profile (menus) page.
            - Verify that the response status is 200.
            - Check that the page contains the title of the created menu.
        """
        # Create a test user
        User.objects.create_user(username='testuser', password='12345')
        
        # Log in the test user
        self.client.login(username='testuser', password='12345')

        # Create a sample menu item for testing
        Menu.objects.create(
            title="Test Menu", 
            slug="test-menu", 
            price=15.99, 
            date_displayed="2024-12-01", 
            image="default.png"
        )

        # Access the menus page (profile page)
        response = self.client.get(reverse('menus:menus'))
        
        # Verify that the page loads successfully and contains the menu title
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Menu")
