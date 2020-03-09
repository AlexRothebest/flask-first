from flask import Flask, render_template, request, redirect

from forms import LoginForm


app = Flask(__name__)


app.config['SECRET_KEY'] = '0024e04941a70cbffb92de30c6c313b7a4d5b6106bc31e42c355709a89cc2938'


@app.route('/')
@app.route('/home/')
def home():
	return render_template('home.html')


@app.route('/tournaments/')
def tournaments():
	return render_template('tournaments.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
	if len(request.form) != 0:
		print(f"\n\n{request.form.get('username')} just logged in with password '{request.form.get('password')}'")

		if request.form.get('remember-me'):
			print('Remember this user!\n\n')
		else:
			print('Do not remember this user!\n\n')


		return redirect('/')

	return render_template('login.html')


if __name__ == '__main__':
	app.run(debug=True)