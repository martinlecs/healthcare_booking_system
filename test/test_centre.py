import pytest
from centre import Centre
from provider import Provider

''' 
Tests to conduct
1 - add provider
2 - add provider thats already there
3 - add invalid provider - pre-condition cant test
4 - remove provider
5 - remove provider thats not there
6 - remove provider by name
'''

@pytest.fixture
def centre_fixture(prov_fixture):
    c1 = Centre("Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    c2 = Centre("Prince of Wales", "Randwick", "Hospital", 1234, 93000000)
    c3 = Centre("Westmead Hospital", 1234, "Hospital", 1234, 93000000)
    c4 = Centre("Randwick Hospital", "Randwick", "Hospital",
                1234, 93000000, [prov_fixture[0], prov_fixture[2]])
    return [c1, c2, c3, c4]


@pytest.fixture
def prov_fixture():
    p1 = Provider("aa@gmail.com", "pwd", "smith", "john", 123, "GP")
    p2 = Provider("bb@gmail.com", "pwd", "smith", "jane", 123, "GP")
    p3 = Provider("cc@gmail.com", "pwd", "sss", "jane", 123, "Physio")
    return [p1, p2, p3]

def test_add_provider(centre_fixture, prov_fixture):
    c = centre_fixture[0]
    c.add_provider(prov_fixture[0])
    assert(len(c.providers) == 1)
    assert(c.services[prov_fixture[0]]== prov_fixture[0].service)

def test_add_provider_duplicate(centre_fixture, prov_fixture):
    c = centre_fixture[3]
    bef = len(c.providers)
    c.add_provider(prov_fixture[0])
    aft = len(c.providers)
    assert(bef == aft)

def test_remove_provider(centre_fixture, prov_fixture):
    c = centre_fixture[3]
    bef = len(c.providers)
    c.rem_provider(prov_fixture[0])
    aft = len(c.providers)
    assert(bef > aft)
    bef = aft
    c.rem_provider(prov_fixture[2])
    aft = len(c.providers)
    assert(bef > aft)
    assert(c.providers == [])
    assert(c.services == {})

def test_remove_provider_not_there(centre_fixture, prov_fixture):
    c = centre_fixture[3]
    bef = len(c.providers)
    res = c.rem_provider(prov_fixture[1])
    aft = len(c.providers)
    assert(bef == aft)
    assert(res == False)

def test_remove_provider_empty(centre_fixture, prov_fixture):
    c = centre_fixture[0]
    c.rem_provider(prov_fixture[0])
    assert(c.providers == [])
