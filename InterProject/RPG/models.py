from tabnanny import verbose
from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=20)
    level = models.IntegerField()
    race = models.CharField(max_length=30)
    attackPower = models.IntegerField()
    defense = models.IntegerField()
    magic = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'

