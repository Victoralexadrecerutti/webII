from pony.orm import Required
from src.config import db

class Registro(db.Entity):
    data_entrada = Required(str)
    animal = Required("Animal")
    zoologico = Required("Zoologico")
