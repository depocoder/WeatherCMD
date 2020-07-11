import requests
list_city = ['Лондон','Шереметьево','Череповец']

for city in list_city:
    url = 'http://wttr.in/{}?nTqum&lang=ru'.format(city)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)