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
        # pr = self.search_provider_name(provider)  # assumes search_centre_name returns an object
        details = vars(provider)
        details.pop("_password")
        return {k.lstrip('_'): v for k, v in details.items()}

    def get_centre_profile(self, centre):
        """
        This function returns a dict that can be used in Flask's templates
        :param centre: name of centre (String)
        :return: dict containing centre attributes
        """
        # ct = self.search_centre_name(centre)
        return {k.lstrip('_'): v for k, v in vars(centre).items()}

if __name__ == "__main__":
    s = SystemManager()
    from provider import *
    p1 = Provider("email", "pass", "le", "martin", "appointments", 2132131, "service")
    print(s.get_provider_profile(p1))
