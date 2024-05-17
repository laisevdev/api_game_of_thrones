from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/characters/', views.show_characters, name='characters'),
    path('api/housescharacters/', views.show_characters_houses, name='houses_characters'),
    path('api/westeroshouses/', views.westeros_houses, name='houses'),
     path('api/housesdetails/', views.houses_details, name='houses_details'),
]