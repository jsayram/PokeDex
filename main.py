#run to start webserver or website
from website import create_app   #the reason we can do this is because website is a python package
# import requests
# import json
# from flask import Flask

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)







# pokemon_name = {}
# for id in range(1,4):
#    # print(f'id:{id}')
#     response_API = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}/')
#     #print(response_API.status_code)
#     data = response_API.text
#     parsed_data = json.loads(data)
#     pokemon_name[id] = parsed_data['name']
    

# print(pokemon_name.get(3))
