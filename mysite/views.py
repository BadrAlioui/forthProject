from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

def home_page(request):
    """
    Render the home page.

    This view simply renders and returns the 'home.html' template.
    """
    return render(request, 'home.html')


def contact_page(request):
    """
    Handle contact form submissions and display the contact page.

    On GET requests, this view renders the 'contact.html' template with an empty ContactForm.
    On POST requests, it validates the submitted form data, sends an email with the provided message,
    shows a success message if the email is sent, and then redirects back to the contact page.
    """
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            title = f"Message from {name} ({email})"
            send_mail(
                title,
                message,
                "studentinstitute2024@gmail.com",
                ["studentinstitute2024@gmail.com"],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    return render(request, 'contact.html', {'form': form})
