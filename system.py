class SystemManager:
    def __init__(self, user_manager, centre_manager):
        self._user_manager = user_manager
        self._centre_manager = centre_manager
        # self._appointment_manager = []
        #Link centres to provider objects
        self.link_centre_provider()

    def search_service(self):
        pass

    def search_provider_name(self, name):
        """
        Returns provider object that matches has a matching name
        :param name: name of provider
        :return: provider object
        """
        return self._user_manager.search_provider(name)

    def search_centre_name(self):
        return self._centre_manager.search_name

    def search_centre_suburb(self):
        return self._centre_manager.search_suburb

    def get_provider_profile(self, provider):
        """
        This function returns a dict that can be used in Flask's templates
        :param provider: a Provider object
        :return: dict containing provider attributes
        """
        # details = vars(provider)
        # details.pop("_password")
        details = provider.get_information()
        return {k.lstrip('_'): v for k, v in details.items()}

    def get_centre_profile(self, centre):
        """
        This function returns a dict that can be used in Flask's templates
        :param centre: a Centre object
        :return: dict containing centre attributes
        """
        details = centre.get_information()
        return {k.lstrip('_'): v for k, v in details.items()}

    def link_centre_provider(self):
        for centre in self._centre_manager.centres:
            for prov in self._user_manager.providers:
                if centre.name.lower() in prov.centres:
                    centre.add_provider(prov)
        
