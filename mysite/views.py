from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail


def home_page(request):
    return render(request, 'home.html')


def contact_page(request):
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
            return HttpResponse('Thanks for your message')
    return render(request, 'contact.html', {'form': form})
