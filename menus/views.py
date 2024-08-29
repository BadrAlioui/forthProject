from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MenuForm
from .models import Menu

def menus_page(request):
    menus = Menu.objects.all().order_by("-date_displayed")
    return render(request, "menus/list.html", context={"menus": menus})

def menu_page(request, slug):
    menu = get_object_or_404(Menu, slug=slug)
    return render(request, "menus/detail.html", context={"menu": menu})

def create_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():  # Vérifie si le formulaire est valide
            form.save()
            return HttpResponseRedirect('/menus/')
    else:
        form = MenuForm()  # Formulaire vide pour une requête GET
    
    return render(request, "menus/create.html", context={"form": form})
