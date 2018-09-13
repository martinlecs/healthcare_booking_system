from centre import Centre
import csv
import pickle
# from appointment import Appointment

class CentreManager:
    def __init__(self):
        self._centres = []

    @property
    def centres(self):
        return self._centres
    
    def add_centre(self, centre):
        if not any(centre.name == c.name for c in self._centres):
            if isinstance(centre.name, str) and isinstance(centre.suburb, str):
                self._centres.append(centre)
        else:
            #error handling
            return False
    
    def add_centre_from_details(self, name, suburb, id, type, phone, providers=[]):
        centre = Centre(name, suburb, id, type, phone, providers)
        return self.add_centre(centre)

    def rem_centre(self, centre):
        if centre in self._centres:
            self._centres.remove(centre)
        elif any(c._name == centre.name for c in self._centres):
            rem = self.rem_centre_by_name(centre.name)
        else:
            #error handling
            return False

    def rem_centre_by_name(self,name):
        for centre in self.centres:
            if name == centre._name:
                rem = centre
                self.rem_centre(rem)
                return rem
        #error handling
        pass


    #Search Functions
    def search_name(self, search):
        if search == "":
            return self._centres
        else:
            centres = []
            search = search.lower()
            for centre in self.centres:
                name = centre.name.lower()
                if (search in name) and search[0] is name[0]:
                    centres.append(centre)
                elif len(search) > len(name):
                    #This is if the user inputs a "correct" search term plus extra letters
                    if name in search:
                        centres.append(centre)
            return centres

    #Performs prefix match on centre suburbs, returns list of centres that match
    def search_suburb(self, search):
        if search == "":
            return self._centres
        else:
            search = search.lower()
            centres = []
            for centre in self.centres:
                suburb = centre.suburb.lower()
                if (search in suburb) and search[0] is suburb[0]:
                    centres.append(centre)
            return centres

    def save_data(self):
        with open('centres.dat', 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_data(cls):
        try:
            with open('centres.dat', 'rb') as file:
                centre_manager = pickle.load(file)
        except IOError:
            centre_manager = CentreManager.bootstrap()
        return centre_manager
    
    @classmethod
    def bootstrap(cls):
        cm = CentreManager()
        with open('health_centres.csv', newline='') as file:
            reader = csv.reader(file, dialect='excel', quotechar="'")
            for row in reader:
                type = row[0].strip()[1:-1]
                id = int(row[1].strip()[1:-1])
                name = row[2].strip()[1:-1]
                phone = row[3].strip()[1:-1]
                suburb = row[4].strip()[1:-1]
                cm.add_centre_from_details(name,suburb, type, id, phone)
                #Need to insert error handling
        return cm



'''
****** Notes for Centre Manager  *******
Need to add Hospital/Medical type to centre, didn't want to for now as it would require changing all the search/init and isn't too vital
Same with centre id and ph number
Add Error handling like EVERYWHERE
'''
