from centre_manager import *

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
        pass

    def search_suburb(self, search):
        centres = []
        for centre in self._centre_manager.centres:
            if (search in centre.suburb) and search[0] is centre.suburb[0]:
                centres.append(centre)
        return centres