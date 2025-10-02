from pony.orm import Required, Set
from src.config import db

class Produto(db.Entity):
    data_validade = Required(str)
    nome = Required(str)
    tipo = Required(str)   # "Ração" ou "Natural"

    fornecedor = Set("FornecedorAlimentos")  # relação 1:N