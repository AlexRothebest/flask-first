from flask import request, jsonify
from flask_login import login_user, logout_user, current_user

from main import db, bcrypt, login_manager

from main.models import User

from api import api


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


@api.route('/login/', methods=['POST'])
def login():
	request_xhr_key = request.headers.get('X-Requested-With')
	if request_xhr_key and request_xhr_key == 'XMLHttpRequest':
		print(request.get_json())

		return 'LOL'

		username = request.json.get('username')
		password = request.data.get('password')
		remember = request.data.get('remember-me') == 'remember-me'


		user = User.query.filter_by(username=username).first()

		print(User.query.all(), username, User.query.filter_by(username=username).first())

		if user is not None and bcrypt.check_password_hash(user.password, password):
			login_user(user, remember=remember)


			print(f'\n\n{username} just logged in with password "{password}"')

			if remember:
				print('Remember this user!\n\n')
			else:
				print('Do not remember this user!\n\n')


			result = {
				'success': True
			}
		else:
			result = {
				'success': False
			}


		return jsonify(result)