from django.shortcuts import render
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.object.all()
    context = {"recipe": recipes}
    return render(request, "recipe/index.html", context)


def About(request):
    return render(request, "recipe/about.html")


def Login(request):
    return render(request, "recipe/index.html")


def SignUp(request):
    return render(request, "recipe/index.html")
