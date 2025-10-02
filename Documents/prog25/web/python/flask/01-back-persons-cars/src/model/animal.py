from pony.orm import Required
from src.config import db

class Animal(db.Entity):
    especie = Required(str)
    habitat = Required(str)
    localidade = Required(str)
    alimentacao = Required(str)