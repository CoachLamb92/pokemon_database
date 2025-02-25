import json
import requests

root_url = "https://pokeapi.co/api/v2/"
pokemon_keyword = "pokemon/"
for i in range(1, 152):
    pokemon_id = i
    pokemon = requests.get(root_url + pokemon_keyword + str(pokemon_id)).json()
    this_pokemon = {}
    this_pokemon['base_experience'] = pokemon["base_experience"]
    this_pokemon['pokemon_id'] = pokemon["id"]
    this_pokemon['name'] = pokemon["name"]
    this_pokemon['abilities'] = [int(ability['ability']['url'].split('/')[-2]) for ability in pokemon["abilities"] if ability['is_hidden']]
    this_pokemon['hp'] = pokemon["stats"][0]['base_stat']
    this_pokemon['attack'] = pokemon["stats"][1]['base_stat']
    this_pokemon['defense'] = pokemon["stats"][2]['base_stat']
    this_pokemon['special-attack'] = pokemon["stats"][3]['base_stat']
    this_pokemon['special-defense'] = pokemon["stats"][4]['base_stat']
    this_pokemon['speed'] = pokemon["stats"][5]['base_stat']
    this_pokemon['types'] = [type["type"]["name"] for type in pokemon["types"]]
    this_pokemon['moves'] = []
    for move in pokemon["moves"]:
        for vg in move['version_group_details']:
            if vg['version_group']['name'] == 'firered-leafgreen':
                this_pokemon['moves'].append({'level_learned_at': vg['level_learned_at'],
                                            'move_learn_method': vg['move_learn_method']['name'],
                                            'move_id': move["move"]["url"].split('/')[-2]})

    with open (f'data/{pokemon_id}.json', 'w') as f:
        json.dump(this_pokemon, f, indent=4)