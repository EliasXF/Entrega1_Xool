from urllib import request
from django.shortcuts import render, redirect
from pet.models import Pet
from pet.forms import formulario_pet
# Create your views here.

def create_pet(request):
    if request.method == 'POST':
        form = formulario_pet(request.POST)

        if form.is_valid():
            Pet.objects.create(
                name = form.cleaned_data['name'],
                type = form.cleaned_data['type'],
                age = form.cleaned_data['age'],
                powertype = form.cleaned_data['powertype'],
                wings = form.cleaned_data['wings'],
                description = form.cleaned_data['description'],
            )
            return redirect(pet_list)

    elif request.method == 'GET':
        form = formulario_pet()
        context = {'form':form}
        return render(request, 'pet/create-pet.html', context = context)

def pet_list(request):

    pets = Pet.objects.all()
    context = {
        'pets':pets
    } 
    return render(request, 'pet/pet-list.html', context=context)