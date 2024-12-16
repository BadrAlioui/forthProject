from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from menus.models import Menu

#https://www.youtube.com/watch?v=LBuyGv3R0IY&t=6s
class TestProfilePage(TestCase):
    def test_profile_view_accessible_for_authenticated_user(self):
        # Crate a user
        User.objects.create_user(username='testuser', password='12345')

        
        self.client.login(username='testuser', password='12345')

        
        Menu.objects.create(title="Test Menu", slug="test-menu", price=15.99, date_displayed="2024-12-01", image="default.png") # Créer un menu pour le test

        
        response = self.client.get(reverse('menus:menus'))  

        
        self.assertEqual(response.status_code, 200)

        
        self.assertContains(response, "Test Menu")
