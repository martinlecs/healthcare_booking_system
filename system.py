from centre_manager import CentreManager

class SystemManager:
    def __init__(self):
        self._user_manager = []
        self._centre_manager = []
        self._appointment_manager = []

    def search_service(self):
        pass

    def search_provider_name(self):
        pass

    def search_centre_name(self):
        return self._centre_manager.search_name

    def search_centre_subrub(self):
        return self._centre_manager.search_suburb
