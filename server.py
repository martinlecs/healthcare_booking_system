from flask import Flask
from flask_login import LoginManager, current_user, login_user
from centre_manager import CentreManager
from user_manager import UserManager
from system import SystemManager


# Instantiate 'global' variables

app = Flask(__name__)
app.secret_key = 'super secret shhhh'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(email):
	return user_manager.get_user(email)


system = SystemManager()
user_manager = UserManager.load_data()
centre_manager = CentreManager.load_data()