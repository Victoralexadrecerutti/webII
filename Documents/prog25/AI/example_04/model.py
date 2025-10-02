from pony.orm import Database, Required, Set, Optional, PrimaryKey, db_session, ConstraintError
from pony.orm import Json
from pony.orm.core import commit

# Initialize the database
db = Database()
db.bind(provider='sqlite', filename=':memory:', create_db=True)

# Define models

class Ingrediente(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    quantidade = Required(float)
    medida = Required(str)
    receita = Required('Receita')

class Receita(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    ingredientes = Set(Ingrediente)
    modo_de_fazer = Required(str)
    url = Required(str)
    opinioes = Set('Opiniao')

class Opiniao(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome_pessoa = Required(str)
    email = Required(str)
    opiniao = Required(str)
    nota = Required(int, min=1, max=5)
    receita = Required(Receita)

# Generate the mapping
db.generate_mapping(create_tables=True)

# Create test data
with db_session:
    # Receita 1
    r1 = Receita(
        nome='Bolo de Cenoura',
        modo_de_fazer='Misture tudo e leve ao forno por 40 minutos.',
        url='https://example.com/bolo-de-cenoura'
    )

    Ingrediente(nome='Cenoura', quantidade=2.0, medida='unidades', receita=r1)
    Ingrediente(nome='Ovos', quantidade=3.0, medida='unidades', receita=r1)
    Ingrediente(nome='Farinha de trigo', quantidade=2.5, medida='xícaras', receita=r1)

    Opiniao(nome_pessoa='João Silva', email='joao@example.com',
            opiniao='Receita fácil e saborosa!', nota=5, receita=r1)

    # Receita 2
    r2 = Receita(
        nome='Panqueca',
        modo_de_fazer='Bata todos os ingredientes e frite em uma frigideira.',
        url='https://example.com/panqueca'
    )

    Ingrediente(nome='Leite', quantidade=1.0, medida='xícara', receita=r2)
    Ingrediente(nome='Ovo', quantidade=1.0, medida='unidade', receita=r2)
    Ingrediente(nome='Farinha de trigo', quantidade=1.0, medida='xícara', receita=r2)

    Opiniao(nome_pessoa='Maria Oliveira', email='maria@example.com',
            opiniao='Deliciosa e rápida de fazer.', nota=4, receita=r2)

    commit()
