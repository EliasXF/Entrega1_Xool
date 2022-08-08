from django.urls import path
from RPG.views import create_character, character_list, search_character

urlpatterns = [
    path('create-character/', create_character, name='create_character'),
    path('character-list/', character_list, name='character_list'),
    path('search-character/', search_character, name='search_character'),
]