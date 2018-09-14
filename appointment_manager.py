from appointment import Appointment
from user import User
from patient import Patient
from provider import Provider


class AppointmentManager:
    def __init__(self):
        self._appointments = []

# getter
@property
def appointments(self):
    return self._appointments


# add appointments given appointment information 
def add_appointment_by_info(self, appointment_id, provider_email, patient_email, centre_name, date, time):
    if not any(appointment.appointment_id == appointment_id for appointment in self._appointments):      
        appointment = Appointment(appointment_id, provider_email, patient_email, centre_name, date, time)
        self._appointments.append(appointment)
        return True # successful.
    else:
        return False # Fail. Already in appointment list.


def remove_appointment(self, appointment_id):
    for a in self._appointments:
        if a.appointment_id == appointment_id:
            self._appointments.remove(a)
            return True 
        else:
            return False # error handling


# sort appointments
# sort by date and time (?)