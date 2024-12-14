from django.test import TestCase
from django.urls import reverse
from mysite.forms import ContactForm


#https://netninja.dev/courses/unit-testing-in-django/lectures/58314037
class TestContactForm(TestCase):
    def test_create_contact_form_when_submittind(self):
        '''Test that the form is valid when submitting'''
        form_data = {
            'name': 'testuser',
            'email': 'test@test.com',
            'message': 'Hello, this is a test message'
        }
        response = self.client.post(reverse('contact'), data=form_data)

        # Check that the form is valid
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        


    
        

        


            