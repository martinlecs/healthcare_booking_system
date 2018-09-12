from flask import Flask
from centre_manager import CentreManager
from user_manager import UserManager

# Instantiate 'global' variables

app = Flask(__name__)
app.secret_key = 'super secret shhhh'

user_manager = UserManager()
centre_manager = CentreManager.load_data()

if __name__ == "__main__":
    for c in centre_manager.centres:
        print(c.name, c.suburb)