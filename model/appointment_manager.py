from model.appointment import Appointment
from model.error import BookingError, DateTimeValidityError, IdentityError
from model.date_validity import date_and_time_valid
import pickle

class AppointmentManager:
    def __init__(self):
        self._appointments = []
        self._next_appt_id = 0
    
    @property
    def appointments(self):
        return self._appointments

    def search_by_id(self, id_num):
        if type(id_num) is int:
            for appt in self._appointments:
                if appt.id == id_num:
                    return appt
        raise IdentityError("Appointment id doesn't exist")

    def __get_appt_id(self):
        appt_id = self._next_appt_id
        self._next_appt_id += 1
        return appt_id
    # add appointments given appointment information
    # If appointment with certain provider, date and time slot doesn't exist
    #   AND the provider and patient is not the same, 
    #       make appointment.
    # Else,
    #       send False
    def make_appt_and_add_appointment_to_manager(self, patient_email, provider_email, centre_id, date, time_slot, reason):
        try:
            date_and_time_valid(time_slot, date)
        except DateTimeValidityError as e:
            raise e
        
        if patient_email.lower() == provider_email.lower():
            raise BookingError("Provider can't book an appointment with themselves")
        
        if not any(appt.provider_email == provider_email and appt.date == date and appt.time_slot == time_slot for appt in self._appointments):      
            appointment = Appointment(self.__get_appt_id(), patient_email, provider_email, centre_id, date, time_slot, reason)
            # self._get_information(self, appointments)
            self._appointments.append(appointment)
            return appointment # successful.
        else:
            raise BookingError("Booking taken") # Fail. Already in appointment list.


    def remove_appointment(self, appointment_id):
        for appt in self._appointments:
            if appt.id == appointment_id:
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