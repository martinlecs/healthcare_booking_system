from server import app, user_manager
from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user
from server import centre_manager, user_manager

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


""" 
Depending on what radio button is selected, uses the respective
user or centre search function which returns a list of appropriate 
objects to iterate through and display
"""
@app.route('/search', methods = ['GET', 'POST'])
def search():
	if request.method == 'POST':
		pass
	services = [''] + user_manager.get_service_names() #Details for the drop down box
	results = []
	error = False #Displays message for no result/no selection
	type_c = True #Displays table for centre/provider details

	#Not the nicest looking code, but just sorts through depending on which category was pressed
	if request.args.get('select', None) is not None:
		query=request.args.get('query')
		select = request.args.get('select','centre_name') #for now
		if select == 'centre_name':
			results = centre_manager.search_name(query)
			type_c = True
		elif select == 'centre_suburb':
			results = centre_manager.search_suburb(query)
			type_c = True
		elif select == 'prov_name':
			results = user_manager.search_name(query)
			type_c = False
		elif select == 'prov_service':
			query = request.args.get('service', "")
			results = user_manager.search_service(query)
			type_c = False
		if(len(results) is 0):
			error = "No matches found"
	else:
		error = "Please select a search category"
		
	return render_template('search.html', services=services, results=results, error=error, type_c=type_c)
