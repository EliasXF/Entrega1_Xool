from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from InterProyect.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rpg/', include('RPG.urls')),
    path('index/', index, name='index')
]
