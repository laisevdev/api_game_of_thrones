import requests
from django.shortcuts import render

def index(request):
    return render(request, 'api/index.html', {})

def show_characters(request): 
    url = 'https://api.gameofthronesquotes.xyz/v1/characters'
    response = requests.get(url)
    data = response.json()
    characters = [character['name'] for character in data]  
    return render(request, 'api/characters.html', {'characters': characters})