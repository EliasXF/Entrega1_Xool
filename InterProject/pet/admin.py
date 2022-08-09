from django.contrib import admin
from pet.models import Pet
# Register your models here.

'''
Formas de registrar un modelo
'''
#admin.site.register(Products)

@admin.register(Pet) #El @ es un decorador de django. Agrega funcionalidades
class Pet_admin(admin.ModelAdmin):
    list_display = ['name', 'type', 'age', 'powertype', 'description']

