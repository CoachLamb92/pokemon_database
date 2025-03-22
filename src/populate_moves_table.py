import json
import requests
from pprint import pprint
from db.connection import connect_to_db, close_connection


db = connect_to_db()

all_gen_1_moves = db.run("SELECT DISTINCT move_id FROM pokemon_moves ORDER BY move_id;")
moves = [move[0] for move in all_gen_1_moves]

root_url = "https://pokeapi.co/api/v2/"
move_keyword = "move/"

for move_id in moves:
    if [move_id] not in db.run("SELECT DISTINCT move_id FROM moves"):
        move = requests.get(root_url + move_keyword + str(move_id)).json()

        if move["power"] == None: move["power"] = -1
        if move["accuracy"] == None: move["accuracy"] = -1

        value_tuple = (move["id"], move["name"], "PLACEHOLDER", move["type"]["name"], move["pp"], move["accuracy"], move["power"], move["damage_class"]["name"])

        query = f"INSERT INTO moves (move_id, move_name, move_description, move_type, powerpoints, accuracy, power, category) VALUES {value_tuple}"

        result = db.run(query)

close_connection(db)