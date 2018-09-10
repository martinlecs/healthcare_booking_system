from patient import Patient
from user import User
from provider import Provider

class Centre:
    def __init__(self, name, suburb, providers=[], services={}):
        self._name = name
        self._suburb = suburb
        self._providers = providers
        self._services = services
        #self._rating = []

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

    # @property
    # def rating(self):
    #     return self._rating

    #Currently taking in provider class
    def add_provider(self, provider):
        if not any(provider.email == p.name for p in self._providers):
            #error handling
            pass        
        else:
            self._providers.append(provider)
            self._services[provider] = provider.service

    def rem_provider(self, provider):
        if provider in self._providers:
            del(self._services[provider])
            self._providers.remove(provider)
        else:
            #error handling
            pass
