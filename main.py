import requests
import json

pokemon_name = {}
for id in range(1,4):
   # print(f'id:{id}')
    response_API = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}/')
    #print(response_API.status_code)
    data = response_API.text
    parsed_data = json.loads(data)
    pokemon_name[id] = parsed_data['name']
    

print(pokemon_name.get(3))



# for location in parsed_data['Andaman and Nicobar Islands']['districtData']['South Andaman']:
#     print(location)

# active_case = parsed_data['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']

#print("Active cases in South Andaman:", active_case)

