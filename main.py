from flask import Flask


app = Flask(__name__)


@app.route('/')
@app.route('/home/')
def home():
	return 'Hello lol! ;)'


@app.route('/lol/')
def lolek():
	return 'Kek)0)))00)0)'


if __name__ == '__main__':
	app.run(debug=True)