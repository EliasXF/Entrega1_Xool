from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from InterProyect.views import index, lists, search_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('search-list/', search_list, name='search-list'),
    path('lists/', lists, name='lists'),
    path('rpg/', include('RPG.urls')),
    path('vehicle/', include('vehicle.urls')),
    path('pet/', include('pet.urls')),
]
