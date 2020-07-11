import requests
cities = ['Лондон','Шереметьево','Череповец']

for city in cities:
    url = 'http://wttr.in/{}?nTqum&lang=ru'.format(city)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)
