from django.shortcuts import render
from django.http import HttpResponse

from .models import Passenger, Plane, Flight

def index(request):
    return HttpResponse("Hello world. You are at the reservation index")

def home(request):
    context = {
        'flights': Flight.objects.all()
    }
    return render(request, 'reservation/home.html', context)

def about(request):
    return render(request, 'reservation/about.html')
