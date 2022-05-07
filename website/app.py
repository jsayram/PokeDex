import requests
import json
from flask import Flask



pokemon_name = {}
for id in range(1,4):
   # print(f'id:{id}')
    response_API = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}/')
    #print(response_API.status_code)
    data = response_API.text
    parsed_data = json.loads(data)
    pokemon_name[id] = parsed_data['name']
    

print(pokemon_name.get(3))
