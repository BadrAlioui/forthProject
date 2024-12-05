from django.test import TestCase
from menus.models import Menu

#https://www.youtube.com/watch?v=GBgRMdjAx_c&t=858s
class MenuModelTest(TestCase):
    def test_model_str(self):
        menu = Menu.objects.create(
            title='Menu Test',
            content='Exemple pour le test.',
            slug='menu-test',
            price=10.00,  # Prix valide
            image='default.png'
        )
        self.assertEqual(str(menu), 'Menu Test')
