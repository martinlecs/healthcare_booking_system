from server import app, user_manager
from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user
from system import SystemManager


login_manager = LoginManager()
login_manager.init_app(app)
system = SystemManager()


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		return redirect(url_for('index'))


@app.route('/provider/<provider>', methods=['GET'])
def provider_profile(provider):
	"""
	Renders a provider profile
	:param user: a Provider object
	:return: renders the provider_profile.html template
	"""
	content = system.get_provider_profile(provider)
	return render_template('provider_profile.html', content=content)


@app.route('/centre/<centre>', methods=['GET'])
def centre_profile(centre):
	"""
	Creates a centre profile page
	:param centre: a Centre object
	:return: renders the centre_profile.html template
	"""
	content = system.get_centre_profile(centre)
	return render_template('centre_profile.html', content=content)

@app.route('/search', methods=['POST'])
def search():
	if request.form['search'] and request.form['type']:
		if "provider" in request.form['type']:
			pass
		else:
			pass
		return render_template('search_results', results=results)
	return redirect(url_for('index'))

@login_manager.user_loader
def load_user(email):
	return user_manager.get_user_by_email(email)