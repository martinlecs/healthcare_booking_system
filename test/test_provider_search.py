import pytest
from centre_manager import CentreManager
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
    p2 = Provider("bb@gmail.com", "pwd", "smith", "jane", 123, "GP")
    p3 = Provider("cc@gmail.com", "pwd", "sss", "jane", 123, "Physio")
    return [p1, p2, p3]


@pytest.fixture
def centre_fixture():
    c1 = Centre("Randwick Hospital", "Randwick")
    c2 = Centre("Prince of Wales", "Randwick")
    c3 = Centre("Westmead Hospital", 1234)
    c4 = Centre("Randwick Hospital", "Randwick")
    return [c1, c2, c3, c4]


@pytest.fixture
def cm(prov_fixture):
    cm = CentreManager()
    c1 = Centre("Randwick Hospital", "Randwick")
    c2 = Centre("Prince of Wales", "Randwick")
    c3 = Centre("Randwick Hospital", "Randwick",
                [prov_fixture[0], prov_fixture[2]])
    c4 = Centre("RPA", "Camperdown", [
                prov_fixture[0], prov_fixture[1], prov_fixture[2]])
    for centre in [c1, c2, c3, c4]:
        cm.add_centre(centre)
    return cm


def test_centre_search_all_name(cm):
    result = cm.search_name("")
    assert(result == cm.centres)


def test_centre_search_all_suburb(cm):
    result = cm.search_suburb("")
    assert(result == cm.centres)


def test_centre_search_name_exact(cm, ):
    text = "Randwick Hospital"
    result = cm.search_name(text)
    for i in result:
        assert(text == i.name)


def test_centre_search_name_prefix(cm):
    text = "Rand"
    result = cm.search_name(text)
    for i in result:
        assert(text in i.name)


def test_centre_search_name_insensitive(cm):
    text = "rAnDwick"
    result = cm.search_name(text)
    assert(result != [])
    for i in result:
        assert(text.lower() in i.name.lower())


def test_centre_search_name_suffix(cm):
    text = "wick"
    result = cm.search_name(text)
    assert(result == [])


def test_centre_search_name_wrong(cm):
    text = "Royal"
    result = cm.search_name(text)
    assert(result == [])


def test_centre_serach_name_longer(cm):
    text = "RPAA"
    result = cm.search_name(text)
    for i in result:
        assert(i.name.lower() in text.lower())


def test_centre_search_all_suburb(cm):
    result = cm.search_suburb("")
    assert(result == cm.centres)


def test_centre_search_suburb_exact(cm):
    text = "Camperdown"
    result = cm.search_suburb(text)
    for i in result:
        assert(text == i.suburb)


def test_centre_search_suburb_prefix(cm):
    text = "Rand"
    result = cm.search_suburb(text)
    for i in result:
        assert(text in i.suburb)


def test_centre_search_suburb_insensitive(cm):
    text = "cAmPerDOWN"
    result = cm.search_suburb(text)
    assert(result != [])
    for i in result:
        assert(text.lower() in i.suburb.lower())


def test_centre_search_suburb_suffix(cm):
    text = "wick"
    result = cm.search_suburb(text)
    assert(result == [])


def test_centre_search_suburb_wrong(cm):
    text = "Parramatta"
    result = cm.search_suburb(text)
    assert(result == [])
