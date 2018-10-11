class Referral():
    def __init__(self, patient, specialist, gp, msg):
        self._patient = patient
        self._specialist = specialist
        self._gp = gp
        self._msg = msg

    @property
    def patient(self):
        return self._patient

    @property
    def specialist(self):
        return self._specialist