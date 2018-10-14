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
        """

        :param owner: user id of person sending the notification
        :param target: user id of person receiving the notification
        :return:
        """
        n = BookingNotification("You have a booking", owner, target)
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





