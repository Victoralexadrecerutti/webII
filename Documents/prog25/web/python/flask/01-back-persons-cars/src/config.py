from pony.orm import Database

db = Database()

# aqui você conecta ao banco depois
# exemplo com SQLite:
# db.bind(provider='sqlite', filename='database.sqlite', create_db=True)