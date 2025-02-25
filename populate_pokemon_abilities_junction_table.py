from db.connection import connect_to_db, close_connection
import json

db = connect_to_db()

for i in range(1, 152):

    with open (f"data/{i}.json", "r") as f:
        poke_dict = json.load(f)
        
    for ability in poke_dict['abilities']:
        value_tuple = (poke_dict['pokemon_id'], ability)
    
        query = f"INSERT INTO pokemon_abilities (pokemon_id, ability_id) VALUES {value_tuple}"

        result = db.run(query)

print(db.run("SELECT * FROM pokemon_abilities"))

close_connection(db)