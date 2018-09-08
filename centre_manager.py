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

    def search_name(self, search):
        centres = []
        for centre in self.centres:
            if (search in centre.name) and search[0] is centre.name[0]:
                centres.append(centre)
            elif len(search) > centre.name:
                #This is if the user inputs a "correct" search term plus extra letters
                if centre.name in search:
                    centres.append(centre)
        return centres

    #Performs prefix match on centre suburbs, returns list of centres that match
    def search_suburb(self, search):
        centres = []
        for centre in self.centres:
            if (search in centre.suburb) and search[0] is centre.suburb[0]:
                centres.append(centre)
        return centres
