from patient import Patient
from user import User
from provider import Provider

class Centre:
    def __init__(self, name, suburb, type, id, phone):
        self._name = name
        self._suburb = suburb
        self._providers = []
        self._type = type
        self._id = id
        self._phone = phone
        self._services = {}
        self._rating = {}
        self._average_rating = 0

    #Getter Methods
    @property
    def name(self):
        return self._name

    @property
    def suburb(self):
        return self._suburb

    @property
    def providers(self):
        return self._providers

    @property
    def services(self):
        return self._services

    @property
    def type(self):
        return self._type
    
    @property
    def id(self):
        return self._id
    
    @property
    def phone(self):
        return self._phone

    @property
    def average_rating(self):
        return self._average_rating

    #Currently taking in provider class
    def add_provider(self, provider):
        if not any(provider.email == p.email for p in self._providers):
            self._providers.append(provider)
            self._services[provider] = provider.service
            return True
        else:
            #error handling
            return False        
    
    def rem_provider(self, provider):
        for p in self.providers:
            if provider.email == p.email:
                rem = p
                self.providers.remove(rem)
                self.services.pop(rem)
                return rem
        else:
            #error handling
            return False

	# add rating to dict, recalculate average rating
    def add_rating(self, patient_email, rating):
        self._rating[patient_email] = rating
        self.__calc_average_rating()

	# pop rating from dictionary
    def remove_rating(self, patient_email):
        self._rating.pop(patient_email, None)

	# private function to recalculate average rating
    def __calc_average_rating(self):
        ratings = list(self._rating.values())
        if len(ratings) > 0:
            self._average_rating = sum(ratings)/float(len(ratings))
        else:
            self._average_rating = 0