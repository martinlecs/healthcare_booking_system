from abc import ABC, abstractmethod

# Is there a need for notification manager?
# are they just stored within the target of the notification?

class NotificationsException(Exception):
    pass

class Notification(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def process_notification(self):
        pass


class NotificationsFactory:

    def __init__(self, message, owner, target, type):
        if type == 'notes':
            pass
        elif type == 'booking':
            pass
        else:
            raise NotificationsException


class AccessNotesNotification(Notification):

    idCounter = 0

    def __init__(self, owner, target, permissions):
        self._message = "Allow {} to access your past consultation notes?".format(owner)
        self._owner = owner
        self._target = target
        AccessNotesNotification.idCounter += 1
        self._id = AccessNotesNotification.idCounter
        self._permissions_manager = permissions

    @property
    def message(self):
        return self._message

    @property
    def id(self):
        return self._id

    def process_notification(self):
        self._permissions_manager.add_permissions(self._owner, self._target)


class BookingNotification(Notification):

    idCounter = 0

    def __init__(self, message, owner, target):
        self._message = message
        self._owner = owner
        self._target = target
        BookingNotification.idCounter += 1
        self._id = BookingNotification.idCounter


    @property
    def message(self):
        return self._message

    @property
    def owner(self):
        return self._owner

    @property
    def target(self):
        return self._target

    @property
    def id(self):
        return self._id

    # patient logs in -> patient books appointment with provider -> provider receives notification
    # -> provider requests access to modify notes from patient(?)

    def process_notification(self, state):
        # if target confirms, it be some sort of form submission
        if state:
            pass
            #remove yourself yourself from notifications queue
            # each person has a list of notifications objects in notifications manager


