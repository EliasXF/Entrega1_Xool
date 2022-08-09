from django.urls import path
from pet.views import create_pet, pet_list

urlpatterns = [
    path('create-pet/', create_pet, name='create_pet'),
    path('pet-list/', pet_list, name='pet_list'),
]