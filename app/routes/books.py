from flask import Blueprint, request, jsonify, current_app
from app.models import BookModel
from flask_jwt_extended import jwt_required


books_blueprint = Blueprint('books', __name__)

def format_id(document):
    """Convert MongoDB ObjectId to string for JSON serialization."""
    document["_id"] = str(document["_id"])
    return document

@books_blueprint.route('/', methods=['GET'])
def get_books():
    """Get a paginated list of books."""
    book_model = BookModel(current_app.db)
    
    page = int(request.args.get('page', 1))  
    per_page = int(request.args.get('per_page', 10)) 

    books = book_model.collection.find().skip((page - 1) * per_page).limit(per_page)
    total_count = book_model.collection.count_documents({})

    return jsonify({
        "total": total_count,
        "page": page,
        "per_page": per_page,
        "books": [format_id(book) for book in books]
    }), 200

@books_blueprint.route('/<string:id>', methods=['GET'])
def get_book(id):
    book_model = BookModel(current_app.db)
    book = book_model.get_by_id(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200

@books_blueprint.route('/', methods=['POST'])
@jwt_required()
def create_book():
    book_model = BookModel(current_app.db)
    data = request.json
    book_id = book_model.create(data)
    return jsonify({"message": "Book created", "id": book_id}), 201

@books_blueprint.route('/<string:id>', methods=['PUT'])
def update_book(id):
    book_model = BookModel(current_app.db)
    data = request.json
    book_model.update(id, data)
    return jsonify({"message": "Book updated"}), 200

@books_blueprint.route('/<string:id>', methods=['DELETE'])
def delete_book(id):
    book_model = BookModel(current_app.db)
    book_model.delete(id)
    return jsonify({"message": "Book deleted"}), 200

@books_blueprint.route('/search', methods=['GET'])
def search_books():
    """Search for books by title or author with optional pagination."""
    book_model = BookModel(current_app.db)
    
    title = request.args.get('title', '').strip()
    author = request.args.get('author', '').strip()
    page = int(request.args.get('page', 1))  
    per_page = int(request.args.get('per_page', 10)) 

    books = book_model.search(title=title, author=author, page=page, per_page=per_page)
    return jsonify(books), 200
