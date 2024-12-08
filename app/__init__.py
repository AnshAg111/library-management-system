from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager
from app.routes.books import books_blueprint
from app.routes.members import members_blueprint

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    jwt = JWTManager(app)
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise Exception("MONGO_URI not set in .env file")
    client = MongoClient(mongo_uri)
    app.db = client.library

    app.register_blueprint(books_blueprint, url_prefix='/books')
    app.register_blueprint(members_blueprint, url_prefix='/members')

    return app
