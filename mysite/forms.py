"""
This module defines the ContactForm used on the contact page.
It collects the user's name, email, and message.
"""

from django import forms

class ContactForm(forms.Form):
    """
    A simple contact form.

    This form gathers a user's name, email, and message to be sent to the site administrators.
    """
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ['name', 'email', 'message']
