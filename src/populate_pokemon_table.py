from db.connection import connect_to_db, close_connection
import json

db = connect_to_db()

for i in range(1, 152):
    with open (f"data/{i}.json", "r") as f:
        poke_dict = json.load(f)
    
    value_tuple = (poke_dict['pokemon_id'], poke_dict['name'], poke_dict['base_experience'], poke_dict['types'][0], poke_dict['types'][1] if len(poke_dict['types']) == 2 else 'NULL', poke_dict['hp'], poke_dict['attack'], poke_dict['defense'], poke_dict['special-attack'], poke_dict['special-defense'], poke_dict['speed'])
    
    query = f"INSERT INTO pokemon (pokemon_id, pokemon_name, base_experience, type_1, type_2, hp_stat, attack_stat, defense_stat, special_attack_stat, special_defense_stat, speed_stat) VALUES {value_tuple}"

    result = db.run(query)

close_connection(db)