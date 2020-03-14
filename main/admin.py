from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from main import app, db

from main.models import User


admin = Admin(app, url='/flask-admin')

admin.add_view(ModelView(User, db.session))