from db.connection import connect_to_db, close_connection
from pprint import pprint

db = connect_to_db()

# pprint(db.run("SELECT * FROM pokemon LIMIT 5;")) # works
# pprint(db.run("SELECT * FROM moves LIMIT 5;")) # works
# pprint(db.run("SELECT * FROM pokemon_moves LIMIT 5;")) # works
result = db.run("SELECT * FROM moves WHERE move_id = 10")[0]
print(result)
_, name, text, type, pp, acc, power, category = result
print(name)
print(text)
print(type)
print(pp)
print(acc)
print(power)
print(category)



close_connection(db)

