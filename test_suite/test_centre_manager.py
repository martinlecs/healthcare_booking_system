import pytest
from model.centre_manager import CentreManager
from model.centre import Centre
from model.provider import Provider

""" 
Unit Tests to run:
1 - Add centre
2 - Add centre that already exists
3 - Add invalid centre
4 - Add provider to centre
4 - Remove Centre
5 - Remove Centre that doesn't exist
6 - Remove from empty list
7 - Add centre from details
8 - Add centre from details that already exists
9 - Add centre from details with invalid details
"""

@pytest.fixture
def centre_fixture():
    c1 = Centre("Randwick Hospital", "Randwick","Hospital",1234,93000000)
    c2 = Centre("Prince of Wales", "Randwick", "Hospital", 1234, 93000000)
    c3 = Centre("Westmead Hospital", 1234, "Hospital", 1234, 93000000)
    c4 = Centre("Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    return [c1,c2,c3,c4]

@pytest.fixture
def prov_fixture():
    p1 = Provider("aa@gmail.com","pwd", "smith", "john", 123, "GP")
    p2 = Provider("bb@gmail.com","pwd","smith", "jane", 123, "GP")
    p3 = Provider("cc@gmail.com","pwd","sss", "jane", 123, "Physio")
    return [p1,p2,p3]

@pytest.fixture
def cm(centre_fixture):
    cm = CentreManager()
    cm.add_centre(centre_fixture[0])
    cm.add_centre(centre_fixture[1])
    return cm

def test_empty_list():
    cm = CentreManager()
    assert(len(cm.centres) == 0)

def test_add_centre(centre_fixture):
    cm = CentreManager()
    cm.add_centre(centre_fixture[0])
    assert(len(cm.centres) == 1)
    cm.add_centre(centre_fixture[1])
    assert(len(cm.centres) == 2)

def test_add_centre_dup(centre_fixture):
    cm = CentreManager()
    cm.add_centre(centre_fixture[0])
    cm.add_centre(centre_fixture[3])
    assert(len(cm.centres) == 1)
     
def test_add_invalid(centre_fixture):
    cm = CentreManager()
    invalid = centre_fixture[2]
    cm.add_centre(centre_fixture[0])
    cm.add_centre(invalid)
    assert(len(cm.centres) == 1)

def test_remove(cm, centre_fixture):
    cm.rem_centre(centre_fixture[0])
    assert(len(cm.centres) == 1)
    assert(centre_fixture[0] not in cm.centres)

def test_remove_by_name(cm):
    name = "Randwick Hospital"
    c = cm.rem_centre_by_name(name)
    assert(c not in cm.centres)
    assert(len(cm.centres) == 1)

def test_remove_duplicate(cm, centre_fixture):
    cm.rem_centre(centre_fixture[3])
    assert(len(cm.centres) == 1)
    assert(centre_fixture[0] not in cm.centres)

def test_remove_not_there(cm,centre_fixture):
    bef = cm.centres
    cm.rem_centre(centre_fixture[2])
    aft = cm.centres
    assert(bef is aft)

def test_remove_empty(centre_fixture):
    cm = CentreManager()
    res = cm.rem_centre(centre_fixture[0])
    assert(res == False)

def test_add_from_details(prov_fixture):
    cm = CentreManager()
    cm.add_centre_from_details("Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    cm.add_centre_from_details(
        "Prince of Wales", "Randwick", "Hospital", 1234, 93000000)
    assert(len(cm.centres) == 2)

def test_add_from_details_duplicate(cm, centre_fixture):
    bef = len(cm.centres)
    res = cm.add_centre_from_details(
        "Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    aft = len(cm.centres)
    assert(bef == aft)
    assert(res == False)

def test_add_from_invalid_details(cm):
    res = cm.add_centre_from_details(
        "Randwick Hospital", 1234, "Hospital", 1234, 93000000)
    assert(res == False)
    assert(len(cm.centres) == 2)

