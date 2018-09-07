from flask import Flask
from user_manager import UserManager

# Instantiate 'global' variables

app = Flask(__name__)
user_manager = UserManager()