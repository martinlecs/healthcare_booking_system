from collections import defaultdict
import pickle
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

        self._patients = patients
        self._providers = providers
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

    def display_all_permissions(self):
        print(self._notes_permissions)


    """  
    Load/Save Data methods:
    load_data checks if there is a pickle file for the users (currently only implemented providers)
    if it does, loads that and returns user manager object, otherwise opens the csv and extracts data
    bootstrap is the init function on 'startup' that performs this
    """
    def save_data(self):
        with open('model/data/permissions.dat', 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_data(cls, patients, providers):
        try:
            with open('model/data/permissions.dat', 'rb') as file:
                permissions = pickle.load(file)
        except IOError:
            permissions = Permissions(patients, providers)
        return permissions



