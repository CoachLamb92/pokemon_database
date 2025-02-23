from fastapi import FastAPI, Response, status
import requests
from pydantic import BaseModel
from fastapi import FastAPI
from pprint import pprint

root_url = "https://pokeapi.co/api/v2/"
pokemon_keyword = "pokemon/"
pokemon_id = 1
poke001 = requests.get(root_url + pokemon_keyword + str(pokemon_id)).json()
this_pokemon = {}
this_pokemon['base_experience'] = poke001["base_experience"]
this_pokemon['pokemon_id'] = poke001["id"]
this_pokemon['name'] = poke001["name"]
this_pokemon['hp'] = poke001["stats"][0]['base_stat']
this_pokemon['attack'] = poke001["stats"][1]['base_stat']
this_pokemon['defense'] = poke001["stats"][2]['base_stat']
this_pokemon['special-attack'] = poke001["stats"][3]['base_stat']
this_pokemon['special-defense'] = poke001["stats"][4]['base_stat']
this_pokemon['speed'] = poke001["stats"][5]['base_stat']
this_pokemon['types'] = [type["type"]["name"] for type in poke001["types"]]
this_pokemon['moves'] = []
for move in poke001["moves"]:
    for vg in move['version_group_details']:
        if vg['version_group']['name'] == 'firered-leafgreen':
            this_pokemon['moves'].append({'name': move["move"]["name"],
                                          'level_learned_at': vg['level_learned_at'],
                                          'move_learn_method': vg['move_learn_method']['name'],
                                          'move_id': move["move"]["url"].split('/')[-2]})

pokemon_list = [this_pokemon]
pprint(pokemon_list)
