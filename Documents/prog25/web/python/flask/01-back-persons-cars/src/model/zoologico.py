from pony.orm import *
#from flask import Flask
from src.config import *

# 1. Instância do Flask e do Pony ORM
#app = Flask(__name__)
#db = Database()

# 2. Definição da Classe (Modelo)
class Zoologico(db.Entity):
    nome = Required(str)
    cep = Required(str)

# 3. Configuração e Mapeamento do Banco de Dados
#db.bind(provider='sqlite', filename=':memory:') # Exemplo com SQLite em memória
#db.generate_mapping(create_tables=True)

# 4. Exemplo de uso
@db_session
def criar_zoologico(nome, cep):
    try:
        novo_zoo = Zoologico(nome=nome, cep=cep)
        print(f"Zoológico '{novo_zoo.nome}' com CEP '{novo_zoo.cep}' criado com sucesso!")
        return novo_zoo
    except Exception as e:
        print(f"Erro ao criar zoológico: {e}")

# 5. Chama a função para criar um novo zoológico
criar_zoologico('Zoo de São Paulo', '04301-000')

# Caso fosse uma aplicação web, o restante do código Flask seguiria aqui.
# if __name__ == '__main__':
#     app.run(debug=True)