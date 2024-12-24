from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MenuForm
from .models import Menu
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


def admin_required(user):
    return user.is_staff


def menus_page(request):
    menus = Menu.objects.all().order_by("-date_displayed")
    return render(request, "menus/list.html", context={"menus": menus})


def menu_page(request, slug):
    menu = get_object_or_404(Menu, slug=slug)
    return render(request, "menus/detail.html", context={"menu": menu})


@user_passes_test(admin_required)
def create_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu created successfully!")
            return HttpResponseRedirect('/menus/')  
        else:
            messages.error(request, "Error. Please check your inputs.")
            # Retourne le formulaire avec les erreurs
            return render(request, "menus/create.html", context={"form": form})
    else:
        form = MenuForm()
    return render(request, "menus/create.html", context={"form": form})
