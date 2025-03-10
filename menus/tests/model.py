"""
This module contains tests for the Menu model.
It ensures that the string representation of a Menu instance works as expected.
"""

from django.test import TestCase
from menus.models import Menu


class MenuModelTest(TestCase):
    """
    Tests for the Menu model.
    """

    def test_model_str(self):
        """
        Test that the __str__ method of the Menu model returns the title.
        This test creates a Menu instance and checks that its
        string representation
        matches the title provided.
        """
        menu = Menu.objects.create(
            title='Menu Test',
            content='Exemple pour le test.',
            slug='menu-test',
            price=10.00,  # Valid price
            image='default.png'
        )
        self.assertEqual(str(menu), 'Menu Test')
