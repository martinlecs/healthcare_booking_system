import pytest
from centre_manager import CentreManager
from centre import Centre
from provider import Provider

@pytest.fixture()
def centre_mgr_fixture():
    mgr = CentreManager()
    mgr.add_centre(Centre("Randwick Hospital", "Randwick"))
    mgr.add_centre(Centre("Randwick Medical Centre", "Randwick"))
    mgr.add_centre(Centre("Prince of Wales", "Randwick"))
    