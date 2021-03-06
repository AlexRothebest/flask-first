from flask_login import UserMixin
from main import db


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)

	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)

	password = db.Column(db.String(100), nullable=False)

	profile_photo = db.Column(db.String(60), nullable=False, default='default.img')


	def __repr__(self):
		return self.username