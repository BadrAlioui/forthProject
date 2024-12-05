from django.test import TestCase
from menus.models import Menu

#https://www.google.com/search?sca_esv=3ddc15aac6af2d0d&rlz=1C1GCCA_en&udm=7&sxsrf=ADLYWIJqjj1gWh2bxlgsTAhGw5YL7JLlRw:1733410165030&q=test.py+models.py&sa=X&ved=2ahUKEwjss4uJ8JCKAxVz_rsIHcQ3A6sQ8ccDegQIERAF&biw=1280&bih=585&dpr=1.5#fpstate=ive&vld=cid:af87c5c4,vid:GBgRMdjAx_c,st:0
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

