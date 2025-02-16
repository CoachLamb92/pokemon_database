from fastapi import FastAPI, Response, status
import requests
from pydantic import BaseModel
from fastapi import FastAPI
from pprint import pprint

root_url = "https://pokeapi.co/api/v2/"
pokemon = "pokemon/bulbasaur"
poke001 = requests.get(root_url + pokemon).json()
this_pokemon = {}
# Abilities key
this_pokemon['abilities'] = [ability['ability']["name"] for ability in poke001["abilities"]]
this_pokemon['base_experience'] = poke001["base_experience"]
this_pokemon['id'] = poke001["id"]
this_pokemon['stats'] = [{stat["stat"]["name"]: stat["base_stat"]}for stat in poke001["stats"]]
this_pokemon['types'] = [type["type"]["name"] for type in poke001["types"]]
this_pokemon['moves'] = [move["move"]["name"] for move in poke001["moves"]]
pprint(this_pokemon)

