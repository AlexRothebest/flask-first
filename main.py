from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user

from forms import LoginForm


app = Flask(__name__)


app.config['SECRET_KEY'] = '0024e04941a70cbffb92de30c6c313b7a4d5b6106bc31e42c355709a89cc2938'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)

	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)

	password = db.Column(db.String(60), nullable=False)


	def __repr__(self):
		return self.username


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

		if user is not None and user.password == password:
			login_user(user)  #, remember=remember)


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


		if len(User.query.filter_by(username=request.form.get('username')).all()) == 0:
			new_user = User(
				username=username,
				email=email,
				password=password
			)
			
			db.session.add(new_user)

			db.session.commit()


			login_user(new_user)


		return redirect('/')


	return render_template('sign-up.html')


@app.route('/logout/')
def logout():
	logout_user()


	return redirect('/')


if __name__ == '__main__':
	app.run(debug=True)