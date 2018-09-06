import pytest
from user_manager import UserManager

# Pytest testing file
# A total of 21 tests
# Testing:
#	empty UserManager (1)
#	adding to patients list (2)
#	adding to provider list (2)
#	removing from patient list (3)
#	removing from provider list (3)
#	searching by patient name (4)
#	searching by provider name (4)
#	search by service (2)

# test new user manager
def test_empty_user_manager():
	um = UserManager()
	assert(len(um.patients) == 0)
	assert(len(um.providers) == 0)


# test adding new to patients
def test_add_new_patient():
	um = UserManager()
	um.add_patient('p1')
	assert('p1' in um.patients)

# test adding an existing patient to patients
def test_add_existing_patient():
	um = UserManager()
	p1 = 'p1'
	p2 = 'p2'
	um.add_patient(p1)
	um.add_patient(p2)
	um.add_patient(p1)
	assert(um.patients == [p1,p2])


# test adding new to providers
def test_add_new_provider():
	um = UserManager()
	um.add_provider('p1')
	assert('p1' in um.providers)

# test adding an existing provider to proiders
def test_add_existing_provider():
	um = UserManager()
	p1 = 'p1'
	p2 = 'p2'
	um.add_provider(p1)
	um.add_provider(p2)
	um.add_provider(p1)
	assert(um.providers == [p1,p2])


# test removing existing from patients

# test removing non-existing from patients

# test removing from empty patients


# test removing existing from providers

# test removing non-existing from providers

# test removing from empty providers


# test search for existing patient by exact name

# test search for existing patient by near exact name

# test search for NON-existing patient by exact name

# test search for NON-existing patient by near exact name


# test search for existing provider by exact name

# test search for existing provider by near exact name

# test search for NON-existing provider by exact name

# test search for NON-existing provider by near exact name


# test search for existing service

# test search for non-existing service 