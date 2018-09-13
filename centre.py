from patient import Patient
from user import User
from provider import Provider

class Centre:
    def __init__(self, name, suburb, providers=[]):
        self._name = name
        self._suburb = suburb
        self._providers = providers
        self._services = {}
        self._rating = [5, 4, 3, 5]
        
        #self._rating = []
        for p in self._providers:
            self._services[p]=p.service

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
    def rating(self):
        return float(sum(self._rating)/float(len(self._rating)))

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
