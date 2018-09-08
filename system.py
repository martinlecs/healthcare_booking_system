from centre_manager import CentreManager

class SystemManager:
    def __init__(self):
        self._user_manager = []
        self._centre_manager = []
        self._appointment_manager = []

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
        :param provider: name of provider
        :return: dict containing provider attributes
        """
        pr = self.search_provider_name(provider)  # assumes search_centre_name returns an object
        return vars(pr)

    def get_centre_profile(self, centre):
        """
        This function returns a dict that can be used in Flask's templates
        :param centre: name of centre
        :return: dict containing centre attributes
        """
        ct = self.search_centre_name(centre)
        return vars(ct)
