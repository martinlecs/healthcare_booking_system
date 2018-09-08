from provider import Provider
from patient import Patient
from centre import Centre
# from appointment import Appointment

class CentreManager:
    def __init__(self):
        self._centres = []

    @property
    def centres(self):
        return self._centres
    
    def add_centre(self, centre):
        if centre in self._centres:
            #error handling
            pass
        else:
            self._centres.append(centre)

    def add_centre_from_details(self, name, suburb,providers=[], services=[]):
        centre = Centre(name, suburb, providers, services)
        self.add_centre(centre)

    def rem_centre(self, centre):
        if centre in self._centres:
            self._centres.remove(centre)
        else:
            #error handling
            pass