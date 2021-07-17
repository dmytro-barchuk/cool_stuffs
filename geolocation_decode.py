"""
https://geopy.readthedocs.io/en/latest/
Принимает на вход текстовую строку с названием населенного пункта и выводи
1. Населенный пункт (Дніпро, Дніпровський район, Дніпропетровська область, 49000-49489, Україна)
2. Координаты (48.4680221, 35.0417711)
"""

from geopy.geocoders import Nominatim

city = str(input('Enter city>>>>>')) + ' ua'

geolocator = Nominatim(user_agent="NewApp4")
location = geolocator.geocode(city)


print(location.address)
print((location.latitude, location.longitude))


import requests

url = f"https://dark-sky.p.rapidapi.com/{location.latitude},{location.longitude}"

payload = "{}"
headers = {
    'x-rapidapi-key': "28329afcbemshad8cf8675b5baaap1b25eejsn96ab38affe97",
    'x-rapidapi-host': 'dark-sky.p.rapidapi.com'
}
params = {
    'lang': 'uk',
    # 'extend': 'hourly',
    'units': 'auto'}

headers = {
    'x-rapidapi-key': '28329afcbemshad8cf8675b5baaap1b25eejsn96ab38affe97',
    'x-rapidapi-host': 'dark-sky.p.rapidapi.com'
}

response = requests.request("GET", url, data=payload, headers=headers, params=params)

print(response.text)

