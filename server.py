from flask import Flask
from model.centre_manager import CentreManager
from model.user_manager import UserManager
from model.appointment_manager import AppointmentManager
from model.system import link_centre_provider


# Instantiate 'global' variables

app = Flask(__name__)
app.secret_key = 'super secret shhhh'

user_manager = UserManager.load_data()
centre_manager = CentreManager.load_data()
link_centre_provider(centre_manager, user_manager)
appt_manager = AppointmentManager.load_data()