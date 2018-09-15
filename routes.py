from server import app, user_manager
from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user
from system import SystemManager
from server import *

login_manager = LoginManager()
login_manager.init_app(app)

@app.context_processor
def inject_services_into_all_templates():
	return dict(services=[''] + user_manager.get_service_names()) #Details for the drop down box


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
	:param user: a Provider email
	:return: renders the provider_profile.html template
	"""
	p = user_manager.get_provider(provider)
	content = p.get_information()
	return render_template('provider_profile.html', content=content)


@app.route('/centre/<centre>', methods=['GET'])
def centre_profile(centre):
	"""
	Creates a centre profile page
	:param centre: a Centre id
	:return: renders the centre_profile.html template
	"""
	c = centre_manager.get_centre_from_id(centre)
	content = system.get_centre_profile(c)
	return render_template('centre_profile.html', content=content)


""" 
Depending on what radio button is selected, uses the respective
user or centre search function which returns a list of appropriate 
objects to iterate through and display
"""
@app.route('/search', methods=['POST'])
def search():
	if request.form['type']:
		query = request.form['search']
		select = request.form.get('type', 'centre_name') #for now
		results = []

		if select == 'c_name':
			results = centre_manager.search_name(query)
			type_c = True
		elif select == 'c_suburb':
			results = centre_manager.search_suburb(query)
			type_c = True
		elif select == 'p_name':
			results = user_manager.search_name(query)
			type_c = False
		else:
			results = user_manager.search_service(select)
			type_c = False

		if not results:
			error = "No matches found"
		else:
			error = "Please select a search category"

		return render_template('search_results.html', results=results, type_c=type_c, error=error)
	else:
		return redirect(url_for('index'))


@login_manager.user_loader
def load_user(email):
	return user_manager.get_user_by_email(email)
