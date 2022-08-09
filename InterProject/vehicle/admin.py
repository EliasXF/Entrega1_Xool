from django.contrib import admin
from vehicle.models import Vehicle

# Register your models here.
@admin.register(Vehicle) #El @ es un decorador de django. Agrega funcionalidades
class Vehicle_admin(admin.ModelAdmin):
    list_display = ['type', 'brand', 'model', 'transmission']

