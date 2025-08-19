from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    contexto = {"numero": 5}
    return render(request, "miapp/info.html", contexto )