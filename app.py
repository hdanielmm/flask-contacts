from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.contacts import contacts
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

SQLAlchemy(app)

app.register_blueprint(contacts)
