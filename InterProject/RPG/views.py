
from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from RPG.models import Character
from RPG.forms import formulario_character
from django.http import HttpResponse
# Create your views here.

def create_character(request):
    if request.method == 'POST':
        form = formulario_character(request.POST)

        if form.is_valid():
            Character.objects.create(
                name = form.cleaned_data['name'],
                level = form.cleaned_data['level'],
                race = form.cleaned_data['race'],
                attackPower = form.cleaned_data['attackPower'],
                defense = form.cleaned_data['defense'],
                magic = form.cleaned_data['magic'],
            )
            return redirect(character_list)

    elif request.method == 'GET':
        form = formulario_character()
        context = {'form':form}
        return render(request, 'rpg/create-character.html', context = context)

def character_list(request):

    characters = Character.objects.all()
    context = {
        'characters':characters
    } 
    return render(request, 'rpg/character-list.html', context=context)

