from db.connection import connect_to_db, close_connection
from pprint import pprint

db = connect_to_db()

pprint(db.run("SELECT * FROM pokemon LIMIT 5;")) # works
pprint(db.run("SELECT * FROM moves LIMIT 5;")) # works
pprint(db.run("SELECT * FROM abilities LIMIT 5;")) # empty
pprint(db.run("SELECT * FROM pokemon_abilities LIMIT 5;")) # empty
pprint(db.run("SELECT * FROM pokemon_moves LIMIT 5;")) # works


close_connection(db)