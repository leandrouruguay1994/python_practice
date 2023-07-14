import requests
from pprint import pprint

API_key = '091153c6d5e45ad7ce5569b116df4040'

city = input('Please, enter one city: ')
base_url = f'http://api.openweathermap.org/data/2.5/weather?appid={API_key}&q={city}'

weather_data = requests.get(base_url).json()

pprint(weather_data)
