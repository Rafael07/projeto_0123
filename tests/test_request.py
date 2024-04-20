import requests

api_pokemon = 'https://pokeapi.co/api/v2/pokemon/'

r = requests.get(api_pokemon)
r.status_code
print(r.status_code)

assert r.status_code == 200
