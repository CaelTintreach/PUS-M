from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('DATABASE_URI'))
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

from application import routes