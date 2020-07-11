import requests
List_City = ['Лондон','Шереметьево','Череповец']

for i in List_City:
    url = 'http://wttr.in/san%20{}?nTqum&lang=ru'.format(i)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)