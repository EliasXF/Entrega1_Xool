from urllib import request
from django.shortcuts import render, redirect
from vehicle.models import Vehicle
from vehicle.forms import formulario_vehicle
# Create your views here.

def create_vehicle(request):
    if request.method == 'POST':
        form = formulario_vehicle(request.POST)

        if form.is_valid():
            Vehicle.objects.create(
                type = form.cleaned_data['type'],
                brand = form.cleaned_data['brand'],
                model = form.cleaned_data['model'],
                doors = form.cleaned_data['doors'],
                transmission = form.cleaned_data['transmission'],
            )
            return redirect(vehicle_list)

    elif request.method == 'GET':
        form = formulario_vehicle()
        context = {'form':form}
        return render(request, 'vehicle/create-vehicle.html', context = context)

def vehicle_list(request):

    vehicles = Vehicle.objects.all()
    context = {
        'vehicles':vehicles
    } 
    return render(request, 'vehicle/vehicle-list.html', context=context)