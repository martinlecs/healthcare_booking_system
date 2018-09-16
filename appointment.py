class Appointment:
    " Appointment class"
    appt_id = 0
    def __init__(self, patient_email, provider_email, centre_id, date, time_slot, reason):
        self._id = self.__set_id()
        self._provider_email = provider_email
        self._patient_email = patient_email
        self._centre_id = centre_id
        self._date = date
        self._time_slot = time_slot
        self._notes = ""
        self._meds = []
        self._reason = reason
        self._past = False

    def get_information(self):
        return { 'id': self._id,
                 'provider_email': self._provider_email,
                 'patient_email': self._patient_email,
                 'centre_id': self._centre_id,
                 'date': self._date,
                 'time_slot': self._time_slot,
                 'notes': self._notes,
                 'meds': self._meds,
                 'reason': self._reason,
                 'past': self._past,
                }

# getters
    @property
    def id(self):
        return self._id

    @property
    def provider_email(self):
        return self._provider_email

    @property
    def patient_email(self):
        return self._patient_email
    
    @property
    def centre_id(self):
        return self._centre_id

    @property
    def date(self):
        return self._date

    @property
    def time_slot(self):
        return self._time_slot

    @property
    def notes(self):
        return self._notes
    
    @property
    def meds(self):
        return self._meds

    @property
    def reason(self):
        return self._reason
    
    @property
    def past(self):
        return self._past
    
    

# setters
    def __set_id(self):
        Appointment.appt_id += 1
        return Appointment.appt_id

    @provider_email.setter
    def provider_email(self, provider_email):
        self._provider_email = provider_email

    @patient_email.setter
    def patient_email(self, patient_email):
        self._patient_email = patient_email

    @centre_id.setter
    def centre_id(self, centre_id):
        self._centre_id = centre_id

    @date.setter
    def date(self, date):
        self._date = date

    @time_slot.setter
    def time_slot(self, time_slot):
        self._time = time_slot

    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @reason.setter
    def reason(self, reason):
        self._reason = reason


    
    def add_meds(self, med):
        med = med.lower()
        if med not in self._meds:
            self._meds.append(med)

    def in_the_past(self):
        self._past = True

   