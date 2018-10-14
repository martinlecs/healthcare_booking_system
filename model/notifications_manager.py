from model.notifications import *
from collections import defaultdict
import pickle

class NotificationsManager():

    def __init__(self, patients, providers, permissions):

        def generate_notifications_matrix(patients, providers):
            d = {}
            d = defaultdict(lambda:[], d)
            for i in patients + providers:
                d[i.email]
            return d

        self._notifications_matrix = generate_notifications_matrix(patients, providers)
        self._permissions_manager = permissions

    def get_all_notifications(self, user_email):
        return self._notifications_matrix[user_email]

    def get_notification(self, user_email, notification_id):
        for n in self._notifications_matrix[user_email]:
            if str(n.id) == str(notification_id):
                return n

    # replace with factory pattern
    def add_notification(self, owner, target):
        """

        :param owner: user id of person sending the notification
        :param target: user id of person receiving the notification
        :return:
        """
        # n = BookingNotification("You have a booking", owner, target)
        n = AccessNotesNotification(owner, target, self._permissions_manager)
        self._notifications_matrix[target].append(n)

    def remove_notification(self, user, notification_id):
        """

        :param user: user email
        :param notification_id:
        :return:
        """
        for n in self._notifications_matrix[user]:
            if str(n.id) == str(notification_id):
                self._notifications_matrix[user].remove(n)


    """  
    Load/Save Data methods:
    load_data checks if there is a pickle file for the users (currently only implemented providers)
    if it does, loads that and returns user manager object, otherwise opens the csv and extracts data
    bootstrap is the init function on 'startup' that performs this
    """
    def save_data(self):
        with open('model/data/notifications.dat', 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_data(cls):
        try:
            with open('model/data/notifications.dat', 'rb') as file:
                notifications = pickle.load(file)
        except IOError:
            notifications = NotificationsManager()
        return notifications




