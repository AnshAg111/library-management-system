from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_blueprint = Blueprint('auth', __name__)

users = {
    "admin": "password123"
}

@auth_blueprint.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a JWT."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check if user exists
    if users.get(username) == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
