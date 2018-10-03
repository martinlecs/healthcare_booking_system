from model.centre_manager import CentreManager
from model.user_manager import UserManager

def link_centre_provider(centre_manager, user_manager):
    for centre in centre_manager.centres:
        for prov in user_manager.providers:
            if centre.name.lower() in prov.centres:
                centre.add_provider(prov)
