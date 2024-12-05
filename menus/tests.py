from django.test import TestCase
from menus.models import Menu


class MenuTestCase(TestCase):
    def test_create_menu(self):
        Menu.objects.create(
            title="Couscous",
            content="Doe",
            slug="sluge",
            price=4,
            
        )
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(Menu.objects.get().title, "Couscous")
        self.assertEqual(Menu.objects.get().content, "Doe")
        self.assertEqual(Menu.objects.get().price, 4)

