from abc import ABC, abstractmethod

# Is there a need for notification manager?
# are they just stored within the target of the notification?

class Notification(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def process_notification(self):
        pass


class AccessNotesNotification(Notification):

    def __init__(self, message, requester, target):
        self._message = message
        self._requester = requester
        self._target = target

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, mssg):
        self._message = mssg

    def process_notification(self, state):
        if state:
            permissions.add_permissions(self._requester, self._target)


class BookingNotification(Notification):

    def __init__(self, message, owner, target):
        self._message = message
        self._owner = owner
        self._target = target

    # patient logs in -> patient books appointment with provider -> provider receives notification
    # -> provider requests access to modify notes from patient(?)

    def process_notification(self, state):
        # if target confirms, it be some sort of form submission
        if state:
            pass
            #remove yourself yourself from notifications queue
            # each person has a list of notifications objects in notifications manager


