from tabnanny import verbose
from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    age = models.IntegerField()
    powertype = models.CharField(max_length=20) 
    wings = models.CharField(max_length=3)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.type
    
    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

