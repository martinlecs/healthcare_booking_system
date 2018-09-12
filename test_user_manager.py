import pytest
from user_manager import UserManager

# Pytest testing file
# A total of 28 tests
# Testing:
#	empty UserManager (1)
#	adding to patients list (2)
#	adding to provider list (2)
#	services get updated appropriately (2)
#	getting service names (1)
#	getting patient object by email (2)
#	getting provider object by email (2)
#	removing from patient list (3)
#	removing from provider list (3)
#	searching by patient name (4)	-- NOT IMPLEMENTED
#	searching by provider name (4)	-- NOT IMPLEMENTED
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
def test_new_service():
	um = UserManager()
	um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	assert(um.get_service_names() == ['GP'])
	assert(um.services['GP'] == ['example@gmail.com'])
	um.add_provider_by_info('exaample2@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'Prac')
	assert(um.get_service_names() == ['GP', 'Prac'])
	assert(um.services['Prac'] == ['exaample2@gmail.com'])

# test new provider added to existing dict
def test_new_provider_to_existing_service():
	um = UserManager()
	um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	um.add_provider_by_info('example2@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	assert(um.get_service_names() == ['GP'])
	assert(um.services['GP'] == ['example@gmail.com', 'example2@gmail.com'])


# Test get service names
def test_get_service_names():
	um = UserManager()
	um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	assert(um.get_service_names() == ['GP'])
	um.add_provider_by_info('exaample2@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'Prac')
	assert(um.get_service_names() == ['GP', 'Prac'])

# test get existing patient object by email
def test_get_existing_patient():
	um = UserManager()
	um.add_patient_by_info('example@gmail.com', 'password', 'Cena', 'John', '02141244235')
	p1 = um.get_patient('example@gmail.com') 
	assert(p1.email == 'example@gmail.com')
	assert(p1.password == 'password')
	
# test get non-existing patient object by non-existing email
def test_get_non_existing_patient():
	um = UserManager()
	p1 = um.get_patient('example@gmail.com') 
	assert(p1 == None)


# test get existing provider obejct by email
def test_get_existing_provider():
	um = UserManager()
	um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '02141244235' ,'GP')
	p1 = um.get_provider('example@gmail.com') 
	assert(p1.email == 'example@gmail.com')
	assert(p1.password == 'password')
	assert(p1.service == 'GP')

# test get non-existing provider object by non-existing email
def test_get_non_existing_provider():
	um = UserManager()
	p1 = um.get_provider('example@gmail.com') 
	assert(p1 == None)

# test removing existing from patients
def test_remove_existing_patient():
	um = UserManager()
	um.add_patient_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223')
	assert(len(um.patients) == 1 )
	assert(um.patients[0].email == 'example@gmail.com')
	assert(um.get_patient('example@gmail.com') is not None)
	assert(um.remove_patient('example@gmail.com'))
	assert(um.patients == [])

# test removing non-existing from patients
def test_remove_non_existing_patient():
	um = UserManager()
	um.add_patient_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223')
	assert(not um.remove_patient('example2@gmail.com'))
	assert(um.patients[0].email == 'example@gmail.com')

# test removing from empty patients
def test_remove_non_existing_patient_from_empty_list():
	um = UserManager()
	assert(not um.remove_patient('example2@gmail.com'))
	assert(um.patients == [])


# test removing existing from providers
def test_remove_existing_provider():
	um = UserManager()
	um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223', 'GP')
	assert(len(um.providers) == 1 )
	assert(um.providers[0].email == 'example@gmail.com')
	assert(um.get_provider('example@gmail.com') is not None)
	assert(um.remove_provider('example@gmail.com'))
	assert(um.providers == [])

# test removing non-existing from providers
def test_remove_non_existing_provider():
	um = UserManager()
	assert(len(um.providers) == 0 )
	assert(not um.remove_provider('example@gmail.com'))
	assert(um.providers == [])

# test removing from empty providers
def test_remove_non_existing_provider_from_empty_list():
	um = UserManager()
	assert(not um.remove_provider('example2@gmail.com'))
	assert(um.providers == [])


# test search for existing patient by exact name

# test search for existing patient by near exact name

# test search for NON-existing patient by exact name

# test search for NON-existing patient by near exact name


# test search for existing provider by exact name

# test search for existing provider by near exact name

# test search for NON-existing provider by exact name

# test search for NON-existing provider by near exact name


# test search for existing service
def test_search_for_existing_service():
	um = UserManager()
	um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	um.add_provider_by_info('example22@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	assert(um.search_service('GP') == ['example@gmail.com', 'example22@gmail.com'])
	um.add_provider_by_info('example2332@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'Psychology')
	assert(um.search_service('Psychology') == ['example2332@gmail.com'])

# test search for non-existing service
def test_search_for_non_existing_service():
	um = UserManager()
	um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	um.add_provider_by_info('example22@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
	assert(um.search_service('GP') == ['example@gmail.com', 'example22@gmail.com'])
	assert(not um.search_service('Psychology'))