from collections import defaultdict
# This class keeps track of what permissions each user in the system has.
# Specifc permissions are required to access certain data


class Permissions:

    def __init__(self, patients, providers):

        def generate_permissions_grid():
            d = defaultdict(dict)
            all_users = patients + providers

            # very unpython
            for i in all_users:
                for j in all_users:
                    d[i.email][j.email] = False
            return d

        self._notes_permissions = generate_permissions_grid()

    def add_permissions(self, a, b):
        """ Adds permission for User a to access/modify User b """
        self._notes_permissions[a][b] = True

    def remove_permissions(self, a, b):
        """ Adds permission for User a to access/modify User b """
        self._notes_permissions[a][b] = False

    def check_permissions(self, a, b):
        """ Checks if User a is able to access/modify User b """
        return self._notes_permissions[a][b]




