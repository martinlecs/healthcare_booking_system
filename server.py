from flask import Flask
from user_manager import UserManager

# Instantiate 'global' variables

app = Flask(__name__)
app.secret_key = 'super secret shhhh'

user_manager = UserManager()
user_manager.add_patient_by_info('pandoa123@gmail.com', '1234','Pando', 'Aran', '04124152')
# centre_manager = CentreManager()