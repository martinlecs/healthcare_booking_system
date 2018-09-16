from flask import Flask
from centre_manager import CentreManager
from user_manager import UserManager
from system import SystemManager

# Instantiate 'global' variables

app = Flask(__name__)
app.secret_key = 'super secret shhhh'

user_manager = UserManager.load_data()
centre_manager = CentreManager.load_data()
system = SystemManager(centre_manager, user_manager)    