class SystemManager():
    def __init__(self, user_manager, appointments_manager, health_centre_manager):
        self._user_manager = user_manager
        self._appointments_manager = appointments_manager
        self._health_centre_manager = health_centre_manager

    @property
    def user_manager(self):
        return self._user_manager

    @property
    def appointments_manager(self):
        return self._appointments_manager

    @property
    def health_centre_manager(self):
        return self.health_centre_manager

    def book_an_appointment(id, patient, provider, centre, date, time, reason, notes ="", medication =""):
        new_appt = appointment(id, patient, provider, centre, date, time, reason, notes, medication, false)
        Patient.add_appointment(new_appt)
        Provider.add_appointment(new_appt)
