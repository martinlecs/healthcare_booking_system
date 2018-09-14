import pytest
from provider import Provider
# Test provider


# Pytest testing file
# Total of 29 tests
# Testing:
#	gettters (6)
#	setters (2)
#	add centre (3)
#	remove centre (3)
#	add rating (5)
#	remove rating (2)
#	calc average rating (4)
#	get availability (2)
# 	make time slot unavailable (2)


def test__non_case_senesitive_setters_and_getters():
	p = Provider('test@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
	assert(p.email == 'test@gmail.com')
	assert(p.password == '1234')
	assert(p.surname == 'McTester')
	assert(p.given_name == 'Test')
	assert(p.provider_no == '124024114')
	assert(p.service == 'Official Tester')

# def test_case_senesitive_setters_and_getters():

# test_add_non_existing_centre

# test_add_existing_centre

# test_add_case_sensitive_centre_name


# test_remove_non_existing_centre

# test_remove_existing_centre

# test_remove_case_sensitive_centre_name


# test_add_int_between_0_and_5_rating

# test_add_int_not_between_0_and_5_rating

# test_add_string_rating

# test_add_rating_for_existing_patient

# test_add_rating_for_non_existing_patient


# test_remove_rating_of_existing_patient

# test_remove_rating_of_non_existing_patient


# test_calc_average_rating_with_1_rating

# test_calc_average_rating_with_more_than_1_rating

# test_calc_average_rating_with_out_ratings

# test_recalc_average_rating_with_out_ratings


# test_get_availability_for_non_existing_time_slot

	# test_get_availability_adds_new_centre

	# test_get_availability_adds_new_date

# test_get_availability_for_existing_time_slot


# test_make_available_time_slot_unavailable

# test_make_non_existing_time_slot_unavailable



