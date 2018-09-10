from server import app, user_manager
from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/', methods=['GET','POST'])
@login_required
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
			return redirect(url_for('index'))
		else:
			return render_template('login.html', invalid_login=True)
	return render_template('login.html', invalid_login=False)

			
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

@login_manager.user_loader
def load_user(email):
	return user_manager.get_user(email)

## Tests ##
# fails at wrong email & wrong pass 
# fails at right email & wrong pass
# succeeds at right email & right password
# fails at empty (or partially empty) submission
# Once logged in, stays logged in after page refresh and page leave
# If not logged in, all pages should redirect to login page
# if logged in, should allow access to all pages user has authority to access
