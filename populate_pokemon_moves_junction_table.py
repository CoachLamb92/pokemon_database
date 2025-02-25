from db.connection import connect_to_db, close_connection
import json

db = connect_to_db()

for i in range(1, 152):

    with open (f"data/{i}.json", "r") as f:
        poke_dict = json.load(f)
        
    for move in poke_dict['moves']:
        value_tuple = (poke_dict['pokemon_id'], move['move_id'], move['level_learned_at'], move['move_learn_method'])
    
        query = f"INSERT INTO pokemon_moves (pokemon_id, move_id, level_learnt, learn_method) VALUES {value_tuple}"

        result = db.run(query)

close_connection(db)