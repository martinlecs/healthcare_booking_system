from server import app, user_manager
from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user
from datetime import date

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		return redirect(url_for('index'))

@login_manager.user_loader
def load_user(email):
	return user_manager.get_user_by_email(email)

@app.route('/booking_form', methods=['GET', 'POST'])
def book():

	date = datetime.date(year, month, day)
