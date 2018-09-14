import pytest
from provider import Provider
# Test provider


# Pytest testing file
# Total of 25 tests
# Testing:
#	gettters (2)
#	setters (2)
#	add centre (3)
#	remove centre (3)
#	add rating (5)
#	remove rating (2)
#	calc average rating (4)
#	get availability (2)
# 	make time slot unavailable (2)

def test_getters():
	p = Provider('test@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
	assert(p.email == 'test@gmail.com'.lower())
	assert(p.password == '1234'.lower())
	assert(p.surname == 'McTester'.lower())
	assert(p.given_name == 'Test'.lower())
	assert(p.provider_no == '124024114'.lower())
	assert(p.service == 'Official Tester'.lower())
	assert(p.appointments == [])
	assert(p.centres == [])
	assert(p.availability == {})
	assert(p.rating == {})
	assert(p.average_rating == 0)

def test_setters():
	p = Provider('test@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
	p.email = 'TESting@gmail.Com'
	assert(p.email == 'testing@gmail.com' )
	p.password = 'WoooWThatsGreat'
	assert(p.password != 'wooowthatsgreat' and p.password == 'WoooWThatsGreat')
	p.surname = 'MCTESTing'
	assert(p.surname == 'mctesting')
	p.given_name = 'TEEEESt'
	assert(p.given_name == 'teeeest')
	p.provider_no = '123123'
	assert(p.provider_no == '123123')
	p.service = 'OFFicial TESTer'
	assert(p.service == 'official tester')


def test_add_non_existing_centre():
	p1 = Provider('test@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
	assert(p1.centres == [])
	p1.add_centre('Randwick Hospital')
	assert('Randwick Hospital'.lower() in p1.centres)


def test_add_existing_centre():
	pp1 = Provider('trst','123', 'sad', '12312', '2323', 'Blah')
	assert(pp1.centres == [])
	pp1.add_centre('Randwick Hospital')
	pp1.add_centre('randwick hospital')
	assert(len(pp1.centres) == 1)


def test_remove_non_existing_centre():
	prov = Provider('testsssss@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
	assert(prov.email == 'testsssss@gmail.com')
	assert(prov.centres == [])
	checker = prov.remove_centre('Randwick Hospital')
	assert(checker is False)

def test_remove_existing_centre():
	prov = Provider('testsssss@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
	assert(prov.centres == [])
	prov.add_centre('rand')
	assert('rand' in prov.centres)
	checker = prov.remove_centre('RAnd')
	assert(checker == True)
	assert(prov.centres == [])


def test_add_int_between_0_and_5_rating():
	p = Provider('1','1','1','','','')
	p.add_rating('patient@gmail.com',3)
	assert('patient@gmail.com' in p.rating.keys())
	assert(p.rating['patient@gmail.com'] == 3)

def test_add_int_NOT_between_0_and_5_rating():
	p = Provider('1','1','1','','','')
	assert(list(p.rating.keys()) == [])
	checker = p.add_rating('patient@gmail.com',-1)
	assert(checker == False)
	assert(list(p.rating.keys()) == [])

def test_add_string_rating():
	p = Provider('1','1','1','','','')
	assert(list(p.rating.keys()) == [])
	checker = p.add_rating('patient@gmail.com','1')
	assert(checker == False)
	assert(list(p.rating.keys()) == [])

def test_add_rating_for_existing_patient():
	p = Provider('1','1','1','','','')
	p.add_rating('patient@gmail.com',3)
	assert(p.rating['patient@gmail.com'] == 3)
	p.add_rating('patient@gmail.com',5)
	assert(p.rating['patient@gmail.com'] == 5)	


def test_remove_rating_of_existing_patient():
	p = Provider('1','1','1','','','')
	p.add_rating('patient@gmail.com',3)
	checker = p.remove_rating('patient@gmail.com')
	assert(checker == True)
	assert(list(p.rating.keys()) == [])

def test_remove_rating_of_non_existing_patient():
	p = Provider('1','1','1','','','')
	checker = p.remove_rating('patient@gmail.com')
	assert(checker == False)
	assert(list(p.rating.keys()) == [])


def test_calc_average_rating_with_1_rating():
	p = Provider('1','1','1','','','')
	p.add_rating('patient@gmail.com',3)
	assert(p.average_rating == 3)

def test_calc_average_rating_with_more_than_1_rating():
	p = Provider('1','1','1','','','')
	p.add_rating('patient@gmail.com',3)
	p.add_rating('222patient@gmail.com',2)
	p.add_rating('pat333ient@gmail.com',5)
	assert(p.average_rating == (3+2+5)/(float(3)))

def test_calc_average_rating_with_out_ratings():
	p = Provider('1','1','1','','','')
	assert(p.average_rating == 0)
	p.add_rating('patient@gmail.com',3)
	p.remove_rating('patient@gmail.com')
	assert(p.average_rating == 0)
	

def test_get_availability_for_non_existing_centre_and_non_existing_date():
	p = Provider('1','1','1','','','')
	p.add_centre('rand')
	p.get_availability('rand', 2018, 2, 3)


# test_make_non_existing_time_slot_unavailable

# test_make_existing_time_slot_unavailable

# test_get_availability_for_existing_date


# test_get_availability_for_non_existing_time_slot

	# test_get_availability_adds_new_centre

	# test_get_availability_adds_new_date

# test_get_availability_for_existing_time_slot


# test_make_available_time_slot_unavailable

# test_make_non_existing_time_slot_unavailable



