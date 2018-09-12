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

# @login_manager.user_loader
# def load_user(email):
# 	return user_manager.get_user_by_email(email)

@app.route('/search', methods = ['GET', 'POST'])
def search():
	if request.method == 'POST':
		pass
	for i in centre_manager.centres:
		print(i.suburb[0])
	test = centre_manager.search_suburb("Randwick")
	print("test: len =", len(test))
	services = ["", "GP", "Pharmacist", "Pathologist"]
	results = []
	if request.args.get('select') is not None:
		query=request.args.get('query')
		select = request.args.get('select','centre_name') #for now
		print(select, query)
		if select == 'centre_name':
			results = centre_manager.search_name(query)
			print(f"Results = {len(results)}")
		elif select == 'centre_suburb':
			results = centre_manager.search_suburb(query)
			print(f"Results = {len(results)}")
		elif select == 'prov_name':
			# results = user_manager.search_name(query)
			pass
		elif select == 'prov_service':
			query = request.args.get('service')
			print(f'query = {query}')
			# results = user_manager.search_service(query)
			
	return render_template('search.html', services=services)
