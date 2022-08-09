from statistics import mode
from django.shortcuts import render
from RPG.models import Character
from vehicle.models import Vehicle

def index(request):
    return render(request, 'index.html', context={})

def lists(request):
    return render(request, 'lists.html', context={})

def search_list(request):
    search = request.GET['search']
    characters = Character.objects.filter(name__icontains=search) 
    vehicles = Vehicle.objects.filter(type__icontains=search) 
    context = { 'characters':characters, 'vehicles':vehicles }
    return render(request, 'search-list.html', context=context)

