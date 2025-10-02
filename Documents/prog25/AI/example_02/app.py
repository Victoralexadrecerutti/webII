
from flask import Flask, request, jsonify
from pony.orm import Database, Required, db_session, select, commit
from flask_cors import CORS

app = Flask(__name__)
db = Database()
db.bind(provider='sqlite', filename='books.sqlite', create_db=True)

CORS(app)

class Book(db.Entity):
    title = Required(str)
    authors = Required(str)
    year = Required(int)
    publisher = Required(str)

db.generate_mapping(create_tables=True)

# ------------------------ Routes ------------------------

@app.route('/books', methods=['POST'])
@db_session
def create_book():
    data = request.json
    book = Book(**data)
    commit()
    return jsonify({"id": book.id}), 201

@app.route('/books', methods=['GET'])
@db_session
def get_books():
    books = select(b for b in Book)[:]
    return jsonify([{
        "id": b.id,
        "title": b.title,
        "authors": b.authors,
        "year": b.year,
        "publisher": b.publisher
    } for b in books])

@app.route('/books/<int:book_id>', methods=['GET'])
@db_session
def get_book(book_id):
    book = Book.get(id=book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({
        "id": book.id,
        "title": book.title,
        "authors": book.authors,
        "year": book.year,
        "publisher": book.publisher
    })

@app.route('/books/<int:book_id>', methods=['PUT'])
@db_session
def update_book(book_id):
    book = Book.get(id=book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    data = request.json
    for key, value in data.items():
        setattr(book, key, value)
    commit()
    return jsonify({"message": "Book updated"})

@app.route('/books/<int:book_id>', methods=['DELETE'])
@db_session
def delete_book(book_id):
    book = Book.get(id=book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    book.delete()
    commit()
    return jsonify({"message": "Book deleted"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
