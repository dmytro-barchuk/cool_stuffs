import requests

url = "https://dark-sky.p.rapidapi.com/33.38044,47.90966"

payload = "{}"
headers = {
    'x-rapidapi-key': "28329afcbemshad8cf8675b5baaap1b25eejsn96ab38affe97",
    'x-rapidapi-host': 'dark-sky.p.rapidapi.com'
}
params = {
    'lang': 'uk',
    'extend': 'hourly',
    'units': 'auto'}

headers = {
    'x-rapidapi-key': '28329afcbemshad8cf8675b5baaap1b25eejsn96ab38affe97',
    'x-rapidapi-host': 'dark-sky.p.rapidapi.com'
}

response = requests.request("GET", url, data=payload, headers=headers, params=params)

print(response.text)
