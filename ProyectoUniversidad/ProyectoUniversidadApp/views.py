from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request): 
    return render (request, "ProyectoUniversidadApp/login.html")

@login_required
def index(request):
     return render (request, "ProyectoUniversidadApp/index.html")

@login_required
def credito(request):
     return render (request, "ProyectoUniversidadApp/credito.html")

@login_required
def financiero(request):
     return render (request, "ProyectoUniversidadApp/financiero.html")

@login_required
def operacional(request):
     return render (request, "ProyectoUniversidadApp/operacional.html")

