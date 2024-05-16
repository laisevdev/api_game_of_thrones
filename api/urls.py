from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/characters/', views.show_characters, name='characters'),
    path('api/housescharacters/', views.show_characters_houses, name='houses_characters'),
]