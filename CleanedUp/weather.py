import requests

city = 'London'
url = 'http://api.weatherapi.com/v1/current.json?key=8c4c62ea9ddc472798b220445250205&q=' + city + '&aqi=no'
reponse = requests.get(url)
weather_json = reponse.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, 'is', description, 'and', temp, 'degrees')

