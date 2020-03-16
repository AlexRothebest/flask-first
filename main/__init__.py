from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager
from flask_bcrypt import Bcrypt

import os


app = Flask(__name__)


app.config['SECRET_KEY'] = '0024e04941a70cbffb92de30c6c313b7a4d5b6106bc31e42c355709a89cc2938'

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://alexthebest:{os.environ['FLASK_FIRST_POSTGRES_PASSWORD']}@localhost/flask_first"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

migrate = Migrate(app, db)

login_manager = LoginManager(app)

bcrypt = Bcrypt(app)


from main.admin import *

from main.routes import *


from api import api


app.register_blueprint(api, url_prefix='/api')