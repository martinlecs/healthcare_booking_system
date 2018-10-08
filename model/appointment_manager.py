from model.appointment import Appointment
import pickle

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
    # If appointment with certain provider, date and time slot doesn't exist
    #   AND the provider and patient is not the same, 
    #       make appointment.
    # Else,
    #       send False
    def make_appt_and_add_appointment_to_manager(self, patient_email, provider_email, centre_id, date, time_slot, reason):
        if not any(appt.provider_email == provider_email and appt.date == date and appt.time_slot == time_slot for appt in self._appointments) and patient_email.lower() != provider_email.lower():      
            appointment = Appointment(patient_email, provider_email, centre_id, date, time_slot, reason)
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

    """  
    Load/Save Data methods:
    load_data checks if there is a pickle file for the users (currently only implemented providers)
    if it does, loads that and returns user manager object, otherwise opens the csv and extracts data
    bootstrap is the init function on 'startup' that performs this
    """
    def save_data(self):
        with open('model/data/appointments.dat', 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_data(cls):
        try:
            with open('model/data/appointments.dat', 'rb') as file:
                appt_manager = pickle.load(file)
        except IOError:
            appt_manager = AppointmentManager()
        return appt_manager