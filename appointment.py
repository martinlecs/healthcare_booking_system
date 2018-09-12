class Appointment:

    def __init__(self, appointment_id, provider_name, centre_name, date, time, reason, notes, medication):
        self._appointment_id = appointment_id
        self._provider_email = provider_email
        self._patient_email = _patient_email
        self._centre_name = centre_name
        self._date = date
        self._time = time
#       self._reason = reason
#       self._notes = notes
#       self._medication = medication
#       self._past = past

# getters
    @property
    def appointmend_id(self):
        return self.appointmend_id

    @property
    def provider_email(self):
        return self.provider_email

    @property
    def patient_email(self):
        return self._patient_email
    
    @property
    def centre_name(self):
        return self.centre_name

    @property
    def date(self):
        return self.date

    @property
    def time(self):
        return self.time

''''
    @property
    def reason(self):
        return self.reason

    @property
    def notes(self):
        return self.notes

    @property
    def medication(self):
        return self.medication
''''


# setters
    @appointment_id.setter
    def appointment_id(self, appointment_id):
        self._appointment_id = appointment_id

    @provider_email.setter
    def provider_email(self, provider_email):
        self._provider_email = provider_email

    @patient_email.setter
    def patient_email(self, patient_email)
        self._patient_email = patient_email

    @centre_name.setter
    def centre_name(self, centre_name):
        self._centre_name = centre_name

    @date.setter
    def date(self, date):
        self._date = date

    @time.setter
    def time(self, time):
        self._time

''''
    @reason.setter
    def reason(self, reason):
        self._reason = reason

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @medication.setter
    def medication(self, medication):
        self._medication = medication

''''    
 
 #   def add_notes(self,):


 #   def add_medications(self,):


