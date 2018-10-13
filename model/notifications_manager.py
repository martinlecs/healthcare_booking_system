from model.notifications import *
from collections import defaultdict

class NotificationsManager():

    def __init__(self, patients, providers):

        def generate_notifications_matrix(patients, providers):
            d = {}
            d = defaultdict(lambda:[], d)
            for i in patients + providers:
                d[i.email]
            return d

        self._notifications_matrix = generate_notifications_matrix(patients, providers)

    def get_notifications(self, user_email):
        return self._notifications_matrix[user_email]

    # replace with factory pattern
    def add_notification(self, owner, target):
        n = BookingNotification("You have a booking", owner, target)
        self._notifications_matrix[target].append(n)

    def remove_notification(self):
        pass





