from server import app, user_manager
from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		email = request.form["email"].lower()
		password = request.form["password"].lower()
		user = user_manager.is_valid_user(email, password)
		if user is not None:
			login_user(user)
			return 'Hi'
			# return redirect(url_for('index'))
		else:
			return render_template('login.html', invalid_login=True)
	return render_template('login.html', invalid_login=False)

			
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@login_manager.user_loader
def load_user(email):
	return user_manager.get_user(email)