from flask import Flask
from appointment import Appointment
from centre_manager import CentreManager
from user_manager import UserManager
from appointment_manager import AppointmentManager
from system import SystemManager

# Instantiate 'global' variables

app = Flask(__name__)
app.secret_key = 'super secret shhhh'

user_manager = UserManager.load_data()
centre_manager = CentreManager.load_data()
appt_manager = AppointmentManager.load_data()
system = SystemManager(user_manager, centre_manager)

A1 = Appointment("jack@gmail.com","toby@gmail.com","1111", "2018-09-20","12:30")
A2 = Appointment("jack@gmail.com","anna@gmail.com","1111","2018-09-20","12:30")
A3 = Appointment("isaac@gmail.com","toby@gmail.com","1111","2018-09-20","12:30")
A4 = Appointment("isaac@gmail.com","anna@gmail.com","1111","2018-09-20","12:30")

jack = user_manager.get_user("jack@gmail.com")
isaac = user_manager.get_user("isaac@gmail.com")
toby = user_manager.get_user("toby@gmail.com")
anna = user_manager.get_user("anna@gmail.com")

jack.add_appointment(A1)
jack.add_appointment(A2)
isaac.add_appointment(A3)
isaac.add_appointment(A4)
toby.add_appointment(A1)
toby.add_appointment(A3)
anna.add_appointment(A2)
anna.add_appointment(A4)

for p in user_manager.providers:
    print(p.email, len(p.appointments))
