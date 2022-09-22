from django.shortcuts import render
from django.template.response import TemplateResponse

'''def index(request):
    return render(request, ".html")'''


def home(request):
    return TemplateResponse(request, "home.html")

def index(request):
    return TemplateResponse(request, "index.html")

def mhome(request):
    return TemplateResponse(request, "mhome.html")

def catalog(request):
    return TemplateResponse(request, "catalog.html")

def profile(request):
    return TemplateResponse(request, "profile.html")

def player(request):
    return TemplateResponse(request, "player.html")
