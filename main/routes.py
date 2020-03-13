from flask import render_template, request, redirect
from flask_login import LoginManager, login_user, logout_user, current_user

from main import app, db, bcrypt, login_manager
from main.models import User


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


@app.route('/')
@app.route('/home/')
def home():
	return render_template('home.html', current_user=current_user)


@app.route('/tournaments/')
def tournaments():
	return render_template('tournaments.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
	if len(request.form) != 0:
		username = request.form.get('username')
		password = request.form.get('password')
		remember = request.form.get('remember-me') == 'remember-me'


		user = User.query.filter_by(username=username).first()

		if user is not None and bcrypt.check_password_hash(user.password, password):
			login_user(user, remember=remember)


			print(f'\n\n{username} just logged in with password "{password}"')

			if remember:
				print('Remember this user!\n\n')
			else:
				print('Do not remember this user!\n\n')


		return redirect('/')


	return render_template('login.html')


@app.route('/sign-up/', methods=['GET', 'POST'])
def sign_up():
	if len(request.form) != 0:
		username = request.form.get('username')
		email = request.form.get('email')
		password = request.form.get('password')


		print(f'\n\n{username} just registered\nE-mail:{email}\nPassword "{password}"\n\n')


		if len(User.query.filter_by(username=username).all()) == 0 and len(User.query.filter_by(email=email).all()) == 0:
			new_user = User(
				username=username,
				email=email,
				password=bcrypt.generate_password_hash(password).decode('UTF-8')
			)
			
			db.session.add(new_user)

			db.session.commit()


			login_user(new_user, remember=True)


		return redirect('/')


	return render_template('sign-up.html')


@app.route('/logout/')
def logout():
	logout_user()


	return redirect('/')