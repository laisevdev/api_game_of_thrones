from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.show_characters, name='characters'),
    path('housescharacters/', views.show_characters_houses, name='houses_characters'),
    path('allinformations/', views.all_info_about_got, name='all_informations'),
    path('houses/', views.westeros_houses, name='houses'),
    path('details/<slug:slug>/', views.details, name='details'),
]