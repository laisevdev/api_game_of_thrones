import requests
from django.http import JsonResponse


def show_characters(request): 
    url = 'https://api.gameofthronesquotes.xyz/v1/characters'
    response = requests.get(url)
    data = response.json()
    characters = data['name']
    return JsonResponse(characters)