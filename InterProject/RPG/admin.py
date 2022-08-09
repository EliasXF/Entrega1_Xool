from django.contrib import admin
from RPG.models import Character

# Register your models here.
@admin.register(Character) #El @ es un decorador de django. Agrega funcionalidades
class Character_admin(admin.ModelAdmin):
    list_display = ['name', 'level', 'race', 'attackPower', 'defense', 'magic']

