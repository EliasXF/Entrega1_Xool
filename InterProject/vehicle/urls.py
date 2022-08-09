from django.urls import path
from vehicle.views import vehicle_list, create_vehicle#, search_vehicle

urlpatterns = [
    path('create-vehicle/', create_vehicle, name='create_vehicle'),
    path('vehicle-list/', vehicle_list, name='vehicle_list'),
    #path('search-vehicle/', search_vehicle, name='search_character'),
]