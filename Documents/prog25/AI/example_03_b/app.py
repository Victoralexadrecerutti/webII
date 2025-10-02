from flask import Flask, request, jsonify
from flask_cors import CORS
from pony.orm import Database, Required, Optional, Set, db_session, PrimaryKey, select

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up Pony ORM with SQLite
db = Database()
db.bind(provider='sqlite', filename='pessoas_e_carros.sqlite', create_db=True)

# Pessoa entity (model)
class Pessoa(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    idade = Required(int)
    cidade = Required(str)
    carros = Set("Carro")  # A Pessoa can have multiple Carros

# Carro entity (model)
class Carro(db.Entity):
    id = PrimaryKey(int, auto=True)
    fabricante = Required(str)
    modelo = Required(str)
    ano = Required(int)
    dono = Required(Pessoa)  # A Carro must have one Pessoa as the owner

db.generate_mapping(create_tables=True)

# Routes

# CRUD for Pessoa

@app.route('/pessoas', methods=['POST'])
@db_session
def create_pessoa():
    data = request.json
    pessoa = Pessoa(nome=data['nome'], idade=data['idade'], cidade=data['cidade'])
    return jsonify({'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade, 'cidade': pessoa.cidade}), 201

@app.route('/pessoas', methods=['GET'])
@db_session
def list_pessoas():
    # obter uma lista das pessoas
    pessoas = Pessoa.select()

    # ESTE COMANDO ABAIXO NÃO FUNCIONA no windows, 
    # ou é algo relacionado a versão de python
    # pessoas = select(p for p in Pessoa)[:]
    
    # o comando abaixo também foi modificado para funcionar no windows
    # ou em outra versão de python, ou algo assim :-/

    # cria lista vazia
    pessoas_json = []
    # percorre as pessoas
    for p in pessoas:
        # adiciona um json da pessoa
        pessoas_json.append({'id': p.id, 'nome': p.nome, 'idade': p.idade, 'cidade': p.cidade})
    # retorna a lista de pessoas em json, ajustando o json
    return jsonify(pessoas_json)

@app.route('/pessoas/<int:id>', methods=['GET'])
@db_session
def get_pessoa(id):
    pessoa = Pessoa.get(id=id)
    if not pessoa:
        return jsonify({'error': 'Pessoa not found'}), 404
    return jsonify({'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade, 'cidade': pessoa.cidade})

@app.route('/pessoas/<int:id>', methods=['PUT'])
@db_session
def update_pessoa(id):
    pessoa = Pessoa.get(id=id)
    if not pessoa:
        return jsonify({'error': 'Pessoa not found'}), 404
    data = request.json
    pessoa.nome = data.get('nome', pessoa.nome)
    pessoa.idade = data.get('idade', pessoa.idade)
    pessoa.cidade = data.get('cidade', pessoa.cidade)
    return jsonify({'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade, 'cidade': pessoa.cidade})

@app.route('/pessoas/<int:id>', methods=['DELETE'])
@db_session
def delete_pessoa(id):
    pessoa = Pessoa.get(id=id)
    if not pessoa:
        return jsonify({'error': 'Pessoa not found'}), 404
    pessoa.delete()
    return jsonify({'message': 'Pessoa deleted successfully'}), 200

# CRUD for Carro

@app.route('/carros', methods=['POST'])
@db_session
def create_carro():
    data = request.json
    dono = Pessoa.get(id=data['dono_id'])
    if not dono:
        return jsonify({'error': 'Pessoa not found'}), 404
    carro = Carro(fabricante=data['fabricante'], modelo=data['modelo'], ano=data['ano'], dono=dono)
    return jsonify({'id': carro.id, 'fabricante': carro.fabricante, 'modelo': carro.modelo, 'ano': carro.ano, 'dono_id': carro.dono.id}), 201

@app.route('/carros', methods=['GET'])
@db_session
def list_carros():
    carros = Carro.select()
    # carros = select(c for c in Carro)[:]

    carros_json=[]
    for c in carros:
        carros_json.append({'id': c.id, 'fabricante': c.fabricante, 'modelo': c.modelo, 'ano': c.ano, 'dono_id': c.dono.id, 'dono_nome': c.dono.nome})
    return jsonify(carros_json)
    #return jsonify([{'id': c.id, 'fabricante': c.fabricante, 'modelo': c.modelo, 'ano': c.ano, 'dono_id': c.dono.id} for c in carros])

@app.route('/carros/<int:id>', methods=['GET'])
@db_session
def get_carro(id):
    carro = Carro.get(id=id)
    if not carro:
        return jsonify({'error': 'Carro not found'}), 404
    return jsonify({'id': carro.id, 'fabricante': carro.fabricante, 'modelo': carro.modelo, 'ano': carro.ano, 'dono_id': carro.dono.id})

@app.route('/carros/<int:id>', methods=['PUT'])
@db_session
def update_carro(id):
    carro = Carro.get(id=id)
    if not carro:
        return jsonify({'error': 'Carro not found'}), 404
    data = request.json
    carro.fabricante = data.get('fabricante', carro.fabricante)
    carro.modelo = data.get('modelo', carro.modelo)
    carro.ano = data.get('ano', carro.ano)
    dono = Pessoa.get(id=data.get('dono_id'))
    if dono:
        carro.dono = dono
    return jsonify({'id': carro.id, 'fabricante': carro.fabricante, 'modelo': carro.modelo, 'ano': carro.ano, 'dono_id': carro.dono.id})

@app.route('/carros/<int:id>', methods=['DELETE'])
@db_session
def delete_carro(id):
    carro = Carro.get(id=id)
    if not carro:
        return jsonify({'error': 'Carro not found'}), 404
    carro.delete()
    return jsonify({'message': 'Carro deleted successfully'}), 200

#if __name__ == '__main__':
#    app.run(debug=True)
