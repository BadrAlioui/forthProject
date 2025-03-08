"""
This module provides views for the Menu application.
It includes views for listing menus, showing details of a menu item,
and allowing admin users to create new menu items.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MenuForm
from .models import Menu
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


def admin_required(user):
    """
    Check if the user is an admin (staff member).

    Returns:
        bool: True if the user is a staff member, False otherwise.
    """
    return user.is_staff


def menus_page(request):
    """
    Display the list of all menu items.

    Retrieves all Menu objects ordered by date_displayed (most recent first)
    and renders them using the 'menus/list.html' template.
    """
    menus = Menu.objects.all().order_by("-date_displayed")
    return render(request, "menus/list.html", context={"menus": menus})


def menu_page(request, slug):
    """
    Display details for a specific menu item.

    Retrieves a Menu object based on the provided slug. If the menu item
    is not found, a 404 error page is returned. The menu details are rendered
    using the 'menus/detail.html' template.
    """
    menu = get_object_or_404(Menu, slug=slug)
    return render(request, "menus/detail.html", context={"menu": menu})


@user_passes_test(admin_required)
def create_menu(request):
    """
    Allow an admin user to create a new menu item.

    Handles GET and POST requests:
        - GET: Displays an empty MenuForm.
        - POST: Validates the submitted form; if valid, saves the new menu item,
          shows a success message, and redirects to the menus list.
          If invalid, it re-renders the form with error messages.

    Returns:
        HttpResponse: The rendered template for creating a menu.
    """
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu created successfully!")
            return HttpResponseRedirect('/menus/')
        else:
            messages.error(request, "Error. Please check your inputs.")
            # Return the form with errors
            return render(request, "menus/create.html", context={"form": form})
    else:
        form = MenuForm()
    return render(request, "menus/create.html", context={"form": form})
