from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MenuForm
from .models import Menu
from django.contrib import messages


def menus_page(request):
    menus = Menu.objects.all().order_by("-date_displayed")
    return render(request, "menus/list.html", context={"menus": menus})


def menu_page(request, slug):
    menu = get_object_or_404(Menu, slug=slug)
    return render(request, "menus/detail.html", context={"menu": menu})


def create_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():  # Vérifie si le formulaire est valide
            form.save()
            messages.success(request, "Menu created successfully!")
            return HttpResponseRedirect('/menus/')  # Redirection après succès
        else:
            messages.error(request, "Error in form submission. Please check your inputs. For exemple, the price must be greater than 0.")
            # Retourne le formulaire avec les erreurs
            return render(request, "menus/create.html", context={"form": form})
    else:
        form = MenuForm()  # Formulaire vide pour une requête GET
    return render(request, "menus/create.html", context={"form": form})

