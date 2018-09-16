from appointment import Appointment
from

class AppointmentManager:
    def __init__(self):
        self._appointments = []

    @property
    def appointments(self):
        return self._appointments

    def search_by_id(self, id_num):
        if type(id_num) is int:
            for appt in self._appointments:
                if appt.id == id_num:
                    return appt
        else:
            return False


    # add appointments given appointment information 
    def make_appt_and_add_appointment_to_manager(self, patient_email, provider_email, centre_id, date, time_slot):
        if not any(appointment.date == date and appointment.time_slot == time_slot for appointment in self._appointments):      
            appointment = Appointment(patient_email, provider_email, centre_id, date, time_slot)
            # self._get_information(self, appointments)
            self._appointments.append(appointment)
            return appointment # successful.
        else:
            return False # Fail. Already in appointment list.


    def remove_appointment(self, appointment_id):
        for appt in self._appointments:
            if appt.appointment_id == appointment_id:
                self._appointments.remove(appt)
                return True 
            else:
                return False # error handling
