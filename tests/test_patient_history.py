import pytest
from model.permissions import Permissions

# Test permissions
@pytest.fixture
def permissions_manager():
    patients = ['minh.le023@gmail.com', 'martin.minh.le@gmail.com']
    providers = ['martin@cseoc.org.au', 'producers@cserevue.org.au']
    return Permissions(patients, providers)

# Test notifications


