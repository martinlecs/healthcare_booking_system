import pytest
from model.provider import Provider
from model.error import *
from model.date_validity import *
# Test provider


# Pytest testing file
# Total of 20 tests
# Testing:
#	gettters (1)
#	setters (1)
#	add centre (2)
#	remove centre (2)
#	add rating (4)
#	remove rating (2)
#	calc average rating (3)
#	get availability (3)
# 	make time slot unavailable (2)

# def test_getters():
# 	p = Provider('test@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
# 	info = p.get_information
# 	assert(info["email"] == 'test@gmail.com'.lower())
# 	assert(info["password"]	== '1234'.lower())
# 	assert(info["surname"] 	== 'McTester'.lower())
# 	assert(info["given_name"] == 'Test'.lower())
# 	assert(info["provider_no"] == '124024114'.lower())
# 	assert(info["service"] == 'Official Tester'.lower())
# 	assert(info["appointments"] == [])
# 	assert(info["centres"] == [])
# 	assert(info["availability"] == {})
# 	assert(info["rating"] == {})
# 	assert(info["average_rating"] == 0)

# def test_setters():
# 	p = Provider('test@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
	
# 	p.email = 'TESting@gmail.Com'
# 	info = p.get_information
# 	assert(info['email'] == 'testing@gmail.com' )
	
# 	p.password = 'WoooWThatsGreat'
# 	info = p.get_information
# 	assert(info['password'] != 'wooowthatsgreat' and info['password'] == 'WoooWThatsGreat')
	
# 	p.surname = 'MCTESTing'
# 	info = p.get_information
# 	assert(info['surname'] == 'mctesting')
	
# 	p.given_name = 'TEEEESt'
# 	info = p.get_information
# 	assert(info['given_name'] == 'teeeest')
	
# 	p.provider_no = '123123'
# 	info = p.get_information
# 	assert(info['provider_no'] == '123123')
	
# 	p.service = 'OFFicial TESTer'
# 	info = p.get_information
# 	assert(info['service'] == 'official tester')


# def test_add_non_existing_centre():
# 	p1 = Provider('test@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
# 	assert(p1.centres == [])
# 	p1.add_centre('Randwick Hospital')
# 	assert('Randwick Hospital'.lower() in p1.centres)

# def test_add_existing_centre():
# 	pp1 = Provider('trst','123', 'sad', '12312', '2323', 'Blah')
# 	assert(pp1.centres == [])
# 	pp1.add_centre('Randwick Hospital')
# 	pp1.add_centre('randwick hospital')
# 	assert(len(pp1.centres) == 1)


# def test_remove_non_existing_centre():
# 	prov = Provider('testsssss@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
# 	assert(prov.email == 'testsssss@gmail.com')
# 	assert(prov.centres == [])
# 	checker = prov.remove_centre('Randwick Hospital')
# 	assert(checker is False)

# def test_remove_existing_centre():
# 	prov = Provider('testsssss@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
# 	assert(prov.centres == [])
# 	prov.add_centre('rand')
# 	assert('rand' in prov.centres)
# 	checker = prov.remove_centre('RAnd')
# 	assert(checker == True)
# 	assert(prov.centres == [])


# def test_add_int_between_0_and_5_rating():
# 	p = Provider('1','1','1','','','')
# 	p.add_rating('patient@gmail.com',3)
# 	assert('patient@gmail.com' in p.rating.keys())
# 	assert(p.rating['patient@gmail.com'] == 3)

# def test_add_int_NOT_between_0_and_5_rating():
# 	p = Provider('1','1','1','','','')
# 	assert(list(p.rating.keys()) == [])
# 	checker = p.add_rating('patient@gmail.com',-1)
# 	assert(checker == False)
# 	assert(list(p.rating.keys()) == [])

# def test_add_string_rating():
# 	p = Provider('1','1','1','','','')
# 	assert(list(p.rating.keys()) == [])
# 	checker = p.add_rating('patient@gmail.com','1')
# 	assert(checker == False)
# 	assert(list(p.rating.keys()) == [])

# def test_add_rating_for_existing_patient():
# 	p = Provider('1','1','1','','','')
# 	p.add_rating('patient@gmail.com',3)
# 	assert(p.rating['patient@gmail.com'] == 3)
# 	p.add_rating('patient@gmail.com',5)
# 	assert(p.rating['patient@gmail.com'] == 5)	


# def test_remove_rating_of_existing_patient():
# 	p = Provider('1','1','1','','','')
# 	p.add_rating('patient@gmail.com',3)
# 	checker = p.remove_rating('patient@gmail.com')
# 	assert(checker == True)
# 	assert(list(p.rating.keys()) == [])

# def test_remove_rating_of_non_existing_patient():
# 	p = Provider('1','1','1','','','')
# 	checker = p.remove_rating('patient@gmail.com')
# 	assert(checker == False)
# 	assert(list(p.rating.keys()) == [])


# def test_calc_average_rating_with_1_rating():
# 	p = Provider('1','1','1','','','')
# 	p.add_rating('patient@gmail.com',3)
# 	assert(p.average_rating == 3)

# def test_calc_average_rating_with_more_than_1_rating():
# 	p = Provider('1','1','1','','','')
# 	p.add_rating('patient@gmail.com',3)
# 	p.add_rating('222patient@gmail.com',2)
# 	p.add_rating('pat333ient@gmail.com',5)
# 	assert(p.average_rating == (3+2+5)/(float(3)))

# def test_calc_average_rating_with_out_ratings():
# 	p = Provider('1','1','1','','','')
# 	assert(p.average_rating == 0)
# 	p.add_rating('patient@gmail.com',3)
# 	p.remove_rating('patient@gmail.com')
# 	assert(p.average_rating == 0)
	
def test_get_availability_invalid_date():
	p = Provider('1','1','1','','','')
	with pytest.raises(DateTimeValidityError) as info:
		checker = p.get_availability('centre', 13, 22, 414)
	with pytest.raises(DateTimeValidityError) as info:
		checker = p.get_availability('centre', 'lol', 22, 414)
		
	

# def test_get_availability_for_non_existing_centre_and_non_existing_but_valid_date():
# 	p = Provider('1','1','1','','','')
# 	# p.add_centre('rand')
# 	checker = p.get_availability('rand', 2018, 9, 20)
# 	assert(checker == False)

# def test_get_availability_for_existing_centre_and_non_existing_date():
# 	p = Provider('1','1','1','','','')
# 	p.add_centre('rand')
# 	val = p.get_availability('rand', 2018, 9, 20)
# 	assert(len(val) == 48)

# def test_get_availability_for_invalid_date():
# 	p = Provider('1','1','1','','','')
# 	p.add_centre('rand')
# 	checker = p.get_availability('rand', 2018, 19, 220)
# 	assert(checker == None)
# 	checker = p.get_availability('rand', 2018, 8, 20)
# 	assert(checker == None)

# def test_make_non_existing_and_available_slots_unavailable():
# 	p = Provider('1','1','1','','','')
# 	p.add_centre('rand')
# 	p.get_availability('rand', 2018, 9, 20)
# 	checker = p.make_time_slot_unavailable('rand', 2018, 9, 20, '08:30')
# 	assert(checker == True)
# 	val = p.get_availability('rand', 2018, 9, 20)
# 	assert('08:30' not in val)
# 	checker = p.make_time_slot_unavailable('rand', 2018, 9, 20, '09:30')
# 	val = p.get_availability('rand', 2018, 9, 20)
# 	assert('08:30' not in val and '09:30' not in val)

# def test_get_availability_for_existing_date():
# 	p = Provider('1','1','1','','','')
# 	p.add_centre('rand')
# 	p.get_availability('rand', 2018, 9, 20)
# 	p.make_time_slot_unavailable('rand', 2018, 9, 20, '08:30')
# 	val = p.get_availability('rand', 2018, 9, 20)
# 	assert('08:30' not in val and type(val) is list)




