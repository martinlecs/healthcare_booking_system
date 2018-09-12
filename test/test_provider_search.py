import pytest
from user_manager import UserManager
from centre import Centre
from provider import Provider

''' 
Items to test
Search Providers
    Search all
    Search by name full
    Search by name prefix
    Search by name suffix
    Search by name substring
    Search by name larger
    Search by name thats not there
**** Done up to here ****
    Search by suburb
    Search by suburb thats not there
    Search with invalid input (i.e integer)
'''


@pytest.fixture
def prov_fixture():
    p1 = Provider("aa@gmail.com", "pwd", "smith", "john", 123, "GP")
    p2 = Provider("bb@gmail.com", "pwd", "smith", "jane", 123, "Surgeon")
    p3 = Provider("cc@gmail.com", "pwd", "sss", "jane", 123, "Physio")
    p4 = Provider("dd@gmail.com", "pwd", "Strange", "Stephen", 123, "GP")
    return [p1, p2, p3, p4]


@pytest.fixture
def centre_fixture():
    c1 = Centre("Randwick Hospital", "Randwick")
    c2 = Centre("Prince of Wales", "Randwick")
    c3 = Centre("Randwick Hospital", "Randwick")
    return [c1, c2, c3]


@pytest.fixture
def um(prov_fixture, centre_fixture):
    um = UserManager()
    um.add_provider_by_info("aa@gmail.com", "pwd", "smith", "john", 123, "GP")
    um.add_provider_by_info("bb@gmail.com", "pwd", "smith", "jane", 123, "Surgeon")
    um.add_provider_by_info("cc@gmail.com", "pwd", "sss", "jane", 123, "Physio")
    um.add_provider_by_info("dd@gmail.com", "pwd", "Strange", "Stephen", 123, "GP")
    return um



def test_provider_search_all_name(um):
    result = um.search_name("")
    assert(result == um.providers)


def test_provider_search_first_name_exact(um):
    text = "jane"
    result = um.search_name(text)
    assert(result != [])
    for i in result:
        assert(text == i.given_name)

def test_provider_search_last_name_exact(um):
    text = "smith"
    result = um.search_name(text)
    assert(len(result)==2)
    for i in result:
        assert(text == i.surname)

def test_provider_search_both_name_exact(um):
    text = "jane smith"
    result = um.search_name(text)
    assert(len(result) == 1)
    for i in result:
        print(i.email)

def test_provider_search_name_prefix(um):
    text = "Step"
    result = um.search_name(text)
    assert(len(result) == 1)
    for i in result:
        assert(text in i.given_name)

def test_provider_search_name_insensitive(um):
    text = "SmITh"
    result = um.search_name(text)
    assert(result != [])
    for i in result:
        assert(text.lower() in i.surname.lower())


def test_provider_search_name_suffix(um):
    text = "phen"
    result = um.search_name(text)
    assert(result == [])


def test_provider_search_name_wrong(um):
    text = "Tim"
    result = um.search_name(text)
    assert(result == [])

def test_service_all(um):
    result = um.search_service("")
    assert(result == um.providers)

def test_provider_search_service_exact(um):
    text = "GP"
    result = um.search_service(text)
    assert(len(result) == 2)
