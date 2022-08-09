from tabnanny import verbose
from django.db import models

# Create your models here.
class Vehicle(models.Model):
    type = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    doors = models.IntegerField()
    transmission = models.CharField(max_length=12)

    def __str__(self):
        return self.model
    
    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
