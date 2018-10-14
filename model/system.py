from model.centre_manager import CentreManager
from model.user_manager import UserManager
from model.error import *

def link_centre_provider(centre_manager, user_manager):
    for centre in centre_manager.centres:
        for prov in user_manager.providers:
            if centre.name.lower() in prov.centres:
                centre.add_provider(prov)

def correct_identity(user, current_user):
    if user.email is not current_user.email:
        raise IdentityError("Wrong user for request")
