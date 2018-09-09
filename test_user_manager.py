import pytest
from user_manager import UserManager

# Pytest testing file
# A total of 21 tests
# Testing:
#	empty UserManager (1)
#	adding to patients list (2)
#	adding to provider list (2)
#	services get updated appropriately
#	getting service names (1)
#	getting patient object by email (2)
#	getting provider object by email (2)
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
	assert(len(um.services) == 0)


# test adding new to patients
def test_add_new_patient():
	um = UserManager()
	assert(um.patients == [])
	cond = um.add_patient_by_info('example@gmail.com', 'password', 'Cena', 'John', '02141244235')
	assert(cond == True)
	assert(len(um.patients) == 1)
	assert(um.patients[0].email == 'example@gmail.com')

	

# test adding an existing patient to patients
def test_add_existing_patient():
	um = UserManager()
	um.add_patient_by_info('1', '1', '1', '1', '1')
	um.add_patient_by_info('1','1','1','1','1')
	assert(len(um.patients) == 1)


# test adding new to providers
def test_add_new_provider():
	um = UserManager()
	cond = um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	assert(cond == True)
	assert(len(um.providers) == 1)
	assert(um.providers[0].email == 'example@gmail.com')


# test adding an existing provider to proiders
def test_add_existing_provider():
	um = UserManager()
	um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	assert(len(um.providers) == 1)

# test new service and provider added to dict

# test new provider added to existing dict


# Test get service names


# test get existing patient obejct by email

# test get non-existing patient object by non-existing email


# test get existing provider obejct by email

# test get non-existing provider object by non-existing email


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