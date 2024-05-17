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

def show_characters_houses(request): 
    url = 'https://api.gameofthronesquotes.xyz/v1/characters'
    response = requests.get(url)
    data = response.json()
    
    characters_with_houses = []
    for character in data:
        house = character.get('house')
        if house is not None:
            house_slug = house.get('slug')
            if house_slug is not None:
                quote = character.get('quotes')
                if quote is not None:
                    character_slug = character.get('slug')
                    if character_slug is not None:
                        characters_with_houses.append({
                            'name': character['name'],
                            'house_slug': house_slug,
                            'quote': character['quotes'][0],
                            'character_slug': character['slug']
                        })    
    return render(request, 'api/houses_characters.html', {'characters_with_houses': characters_with_houses})

def westeros_houses(request):
    url = 'https://api.gameofthronesquotes.xyz/v1/houses'
    response = requests.get(url)
    data = response.json()

    houses = [house['slug'].upper() for house in data]
    return render(request, 'api/houses.html', {'houses': houses})




