from flask import Flask, request, jsonify, abort
from pony.orm import Database, PrimaryKey, Required, db_session, select

# Initialize Flask app
app = Flask(__name__)

# adding CORS support
from flask_cors import CORS
CORS(app)

# Setup Pony ORM and bind to SQLite
db = Database()
db.bind(provider='sqlite', filename='people.sqlite', create_db=True)

# Define the Person entity
class Person(db.Entity):
    id = PrimaryKey(int, auto=True)  # Auto-incremented ID
    name = Required(str)
    email = Required(str)
    phone = Required(str)
    dob = Required(str)  # ISO format (e.g., "1990-01-01")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "dob": self.dob
        }

# Create tables
db.generate_mapping(create_tables=True)

# --- Routes ---

# Create a new person
@app.route('/persons', methods=['POST'])
@db_session
def create_person():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "email", "phone", "dob")):
        abort(400, "Missing fields")
    person = Person(
        name=data["name"],
        email=data["email"],
        phone=data["phone"],
        dob=data["dob"]
    )
    return jsonify(person.to_dict()), 201

# Get all persons
@app.route('/persons', methods=['GET'])
@db_session
def get_all_persons():
    people = select(p for p in Person)[:]
    return jsonify([p.to_dict() for p in people])

# Get a single person by ID
@app.route('/persons/<int:person_id>', methods=['GET'])
@db_session
def get_person(person_id):
    person = Person.get(id=person_id)
    if not person:
        abort(404)
    return jsonify(person.to_dict())

# Update a person
@app.route('/persons/<int:person_id>', methods=['PUT'])
@db_session
def update_person(person_id):
    person = Person.get(id=person_id)
    if not person:
        abort(404)
    data = request.get_json()
    for field in ["name", "email", "phone", "dob"]:
        if field in data:
            setattr(person, field, data[field])
    return jsonify(person.to_dict())

# Delete a person
@app.route('/persons/<int:person_id>', methods=['DELETE'])
@db_session
def delete_person(person_id):
    person = Person.get(id=person_id)
    if person:
        person.delete()
        return jsonify({"result": "deleted"})
    else:
        abort(404)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
