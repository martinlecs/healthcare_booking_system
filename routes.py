from server import app, user_manager
from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user
from provider import *
from system import *
from centre import *


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

@app.route('/provider/<user>', methods=['GET'])
def provider_profile(user):
	# do user lookup to checl of valid
	s = SystemManager()
	p = Provider("email", "pass", "le", "martin", "appointments", 2132131, "service")
	content = s.get_provider_profile(p)
	return render_template('provider_profile.html', content=content)

@app.route('/centre/<centre>', methods=['GET'])
def centre_profile(centre):
	# Normally you would have to do a lookup
	s = SystemManager()
	c = Centre("Hospital", "Randwick")
	content = s.get_centre_profile(c)
	return render_template('centre_profile.html', content=content)


@login_manager.user_loader
def load_user(email):
	return user_manager.get_user_by_email(email)