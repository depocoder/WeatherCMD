import requests

cities = ['Лондон','Шереметьево','Череповец']
payload = {
    'n':'',
    'T':'',
    'q':'',
    'u':'',
    'm':'',
    '&lang':'ru'}


for city in cities:
    url = 'http://wttr.in/{}'.format(city)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)