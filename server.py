from flask import Flask
from user_manager import UserManager

# Instantiate 'global' variables

app = Flask(__name__)
app.secret_key = 'super secret shhhh'

user_manager = UserManager()
# centre_manager = CentreManager()