from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)


app.config['SECRET_KEY'] = '0024e04941a70cbffb92de30c6c313b7a4d5b6106bc31e42c355709a89cc2938'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)

login_manager = LoginManager(app)

bcrypt = Bcrypt(app)


from main.routes import *