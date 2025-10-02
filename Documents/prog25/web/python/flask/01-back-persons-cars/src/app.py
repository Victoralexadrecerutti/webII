from pony.orm import db_session
from src.config import db
from src.model import Produto, FornecedorAlimentos, Registro, Animal, Zoologico

# conecta ao banco
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

# exemplo de inserção
with db_session:
    produto1 = Produto(data_validade="2025-12-31", nome="Carne Fresca", tipo="Natural")
    fornecedor1 = FornecedorAlimentos(nome="Alimentos SA", cnpj="12.345.678/0001-90", produto=produto1)
    animal1 = Animal(nome="Leão", especie="Panthera leo")
    zoo1 = Zoologico(nome="Zoológico Central", localizacao="São Paulo")
    registro1 = Registro(data_entrada="2025-09-15", animal=animal1, zoologico=zoo1)
