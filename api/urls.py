from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.show_characters, name='characters'),
    path('housescharacters/', views.show_characters_houses, name='houses_characters'),
    path('housesdetails/', views.houses_details, name='houses_details'),
    path('houses/', views.westeros_houses, name='houses'),
    path('details/<slug:slug>/', views.details, name='details'),
]