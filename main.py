import os
import requests
import json

base_url = "https://pokeapi.co/api/v2/pokemon/"

pokedex = []

output_directory = "C:/Users/jorda/PycharmProjects/pythonProject/Jsons pokemon"

os.makedirs(output_directory, exist_ok=True)

for pokemon_id in range(1, 1011):
    response = requests.get(f"{base_url}{pokemon_id}")

    if response.status_code == 200:
        pokemon_data = response.json()

        json_filename = os.path.join(output_directory, f"{pokemon_data['name']}.json")

        with open(json_filename, "w") as json_file:
            json.dump(pokemon_data, json_file)

        print(f"dados salvos {pokemon_data['name']} salvos em {json_filename}")

    else:
        print(f"Falha ao obter dados do Pokémon {pokemon_id}")
