from django.test import TestCase
from django.urls import reverse
from menus.models import Menu
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

with open(r'C:\Users\badralil\Desktop\forthProject\media\images\couscous.jpg', 'rb') as img:
    image = SimpleUploadedFile(name='test_image.jpg',
                                   content = img.read(),
                                   content_type='image/jpeg')

# https://www.youtube.com/watch?v=RR7wANxu5gk&t=310s
class MenuFormTest(TestCase):
    def test_menu_form_valid_data(self):
        
        form_data = {
            'title': 'Menu Test',
            'content': 'Example for the test.',
            'slug': 'menu-test',
            'price': 10.00,
            'image': image,
        }
        admin_user = User.objects.create_superuser(username='admin', password='admin123')
        self.client.login(username='admin', password='admin123')

        
        response = self.client.post(reverse('menus:create'), data=form_data)

        # Check the redirection after success
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Menu.objects.filter(title='Menu Test').exists())

    def test_menu_form_no_data(self):
        # Create an admin user and log them in
        admin_user = User.objects.create_superuser(username='admin', password='admin123')
        self.client.login(username='admin', password='admin123')

        # Send a POST request with empty data
        response = self.client.post(reverse('menus:create'), data={})

        # Check that the form is returned with HTTP status 200
        self.assertEqual(response.status_code, 200)

        # Make sure the context contains the form
        self.assertTrue('form' in response.context)

        # Analyze the form to validate the errors
        form = response.context['form']
        self.assertFalse(form.is_valid())  
        self.assertIn('title', form.errors)  
        self.assertIn('slug', form.errors)  
        self.assertIn('price', form.errors) 

        # Check that no object was created in the database
        self.assertFalse(Menu.objects.exists())
