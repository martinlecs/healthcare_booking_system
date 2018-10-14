import pytest
from model.notifications_manager import NotificationsManager
from model.permissions import Permissions
from model.patient import Patient
from model.provider import Provider


# Test permissions
@pytest.fixture
def patients():
    p1 = Patient('example1@gmail.com', 'password1', 'Cena1', 'John1', '1')
    p2 = Patient('example2@gmail.com', 'password2', 'Cena2', 'John2', '2')
    p3 = Patient('example2@gmail.com', 'password3', 'Cena3', 'John3', '3')
    return [p1,p2,p3]


@pytest.fixture
def providers():
    p1 = Provider("aa@gmail.com","pwd", "smith", "john", 123, "GP")
    p2 = Provider("bb@gmail.com","pwd","smith", "jane", 123, "GP")
    p3 = Provider("cc@gmail.com","pwd","sss", "jane", 123, "Physio")
    return [p1,p2,p3]


@pytest.fixture
def permissions_manager(patients, providers):
    return Permissions(patients, providers)


def test_no_permissions(permissions_manager):
    assert permissions_manager.check_permissions('aa@gmail.com', 'example1@gmail.com') is False
    assert permissions_manager.check_permissions('aa@gmail.com', 'bb@gmail.com') is False
    assert permissions_manager.check_permissions('aa@gmail.com', 'aa@gmail.com') is False
    assert permissions_manager.check_permissions('example1@gmail.com', 'example2@gmail.com') is False


def test_with_permissions(permissions_manager):
    permissions_manager.add_permissions('aa@gmail.com', 'example1@gmail.com')
    assert permissions_manager.check_permissions('aa@gmail.com', 'example1@gmail.com') is True
    assert permissions_manager.check_permissions('aa@gmail.com', 'example2@gmail.com') is False
    assert permissions_manager.check_permissions('aa@gmail.com', 'aa@gmail.com') is False


# Test notification manager
@pytest.fixture
def notifications_manager(patients, providers, permissions_manager):
    n = NotificationsManager(patients, providers, permissions_manager)
    n.generate_matrix()
    return n


def test_no_notifications(notifications_manager):
    assert len(notifications_manager.get_all_notifications('aa@gmail.com')) == 0
    assert len(notifications_manager.get_all_notifications('example1@gmail.com')) == 0
    assert len(notifications_manager.get_all_notifications('bb@gmail.com')) == 0
    assert len(notifications_manager.get_all_notifications('cc@gmail.com"')) == 0

def test_with_notifications(notifications_manager):
    notifications_manager.add_notification('example1@gmail.com', 'aa@gmail.com')
    assert len(notifications_manager.get_all_notifications('aa@gmail.com')) == 1
    notifications_manager.add_notification('example1@gmail.com', 'aa@gmail.com')
    assert len(notifications_manager.get_all_notifications('aa@gmail.com')) == 2
    notifications_manager.add_notification('aa@gmail.com', 'example1@gmail.com')
    assert len(notifications_manager.get_all_notifications('example1@gmail.com')) == 1




