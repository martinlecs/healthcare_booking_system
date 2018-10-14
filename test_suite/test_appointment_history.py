import pytest
from model.user_manager import UserManager
from model.centre_manager import CentreManager
from model.appointment_manager import AppointmentManager
from model.appointment import Appointment
from model.error import *
from datetime import datetime, date, time

''' 
Unit tests to run
Setup: Setup provider + user. Create appointments, present and past
Get appointments: Check returned appointments
Get past appointments: patient and provider
Check exceptions
    create second user:
    Access wrong appointment history: raise identity error
    Access specific appointment: raise identity error
    Appointment doesn't exist: Raise 404 error

Don't need to check incorrect or double booking, checked in different unit tests
'''

@pytest.fixture
def centres():
    cm = CentreManager.bootstrap()
    return [cm.centres[0], cm.centres[1]]

@pytest.fixture
def user_manager():
    um = UserManager.bootstrap()
    return um

@pytest.fixture
def appointment_manager():
    am = AppointmentManager()
    return am

@pytest.fixture
def patients(user_manager):
    p1 = user_manager.patients[0]
    p2 = user_manager.patients[1]
    return [p1, p2]

@pytest.fixture
def providers(user_manager):
    p1 = user_manager.providers[0]
    p2 = user_manager.providers[1]
    return [p1, p2]

@pytest.fixture
def appointments(appointment_manager, patients, providers, centres):
    c1 = centres[0]
    date1 = "2018-11-20"
    time1 = "13:00"
    time2 = "14:30"
    a1 = appointment_manager.make_appt_and_add_appointment_to_manager(patients[0].email, providers[0].email, c1,date1, time1, "")    
    a2 = appointment_manager.make_appt_and_add_appointment_to_manager(patients[0].email, providers[1].email, c1,date1, time2, "")    
    a3 = appointment_manager.make_appt_and_add_appointment_to_manager(patients[1].email, providers[0].email, c1,date1, time2, "")
    a4 = appointment_manager.make_appt_and_add_appointment_to_manager(patients[1].email, providers[0].email, c1,"2018-10-20", time2, "")
    a4._past = True
    return [a1, a2, a3, a4]

def test_current_appointment_number_patient(patients, providers, appointments, centres):
    p1 = patients[0]
    p1.add_appointment(appointments[0])
    p1.add_appointment(appointments[1])
    res = len(p1.get_upcoming_appointments())
    assert(res == 2)
    
def test_current_appointment_number_provider(patients, providers, appointments, centres):
    p1 = providers[0]
    p1.add_appointment(appointments[0])
    p1.add_appointment(appointments[2])
    res = len(p1.get_upcoming_appointments())
    assert(res == 2)

def test_past_appointment_number_patient(patients, providers, appointments, centres):
    p1 = patients[0]
    p1.add_appointment(appointments[0])
    p1.add_appointment(appointments[1])
    res = len(p1.get_upcoming_appointments())
    assert(res == 2)

def test_past_appointment_number_provider(patients, providers, appointments, centres):
    p1 = patients[0]
    p1.add_appointment(appointments[3])
    p1.add_appointment(appointments[0]) #add current to see it isn't counted
    res = len(p1.get_past_appointments())
    assert(res == 1)


def test_identity_error(patients):
    from model.system import correct_identity
    with pytest.raises(IdentityError) as error:
        correct_identity(patients[0], patients[1])
