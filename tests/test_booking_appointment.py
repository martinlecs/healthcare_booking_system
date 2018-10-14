import pytest
from model.user_manager import UserManager
from model.centre_manager import CentreManager
from mode.appointment_manager import AppointmentManager
from model.provider import Provider
from model.patient import Patient
from model.appointment import Appointment
from model.error import IdentityError, BookingError
from model.date_validity import date_and_time_valid
from datetime import date, datetime, time

'''
****** TESTS BREAK DOWN ********
Testing the booking appointment process
Total of ... tests
Testing:
	valid date and time
	provider can't book a time with self
	valid booking
		valid provider and centre
		valid 'reason'
'''

@pytest.fixure
def prov_fixture():
	p1 = Provider("aa@gmail.com", "pwd", "smith", "john", 123, "GP")
    p2 = Provider("bb@gmail.com", "pwd", "smith", "jane", 123, "GP")
    p3 = Provider("cc@gmail.com", "pwd", "sss", "jane", 123, "Physio")
    return [p1, p2, p3]

@pytest.fixture
def patient_fixture():
	p1 = Patient("dd@gmail.com", "pwd", "Goldstein", "Mark", "126578445")
	p2 = Patient("ee@gmail.com", "pwd", "Goldstein", "Lizi", "124975")
	p3 = Patient("ff@gmail.com", "pwd", "Goldstein", "Jakob", "1743241")
	return [p1, p2, p3]

@pytest.fixture
def centre_fixture():
    c1 = Centre("Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    c2 = Centre("Prince of Wales", "Randwick", "Hospital", 1234, 93000000)
    c3 = Centre("Westmead Hospital", 1234, "Hospital", 1234, 93000000)
    c4 = Centre("Randwick Hospital", "Randwick", "Hospital",
                1234, 93000000)
    return [c1, c2, c3, c4]

@pytest.fixture
def um_fixture():
	um = UserManager()
	um.add_patient_by_info("dd@gmail.com", "pwd", "Goldstein", "Mark", "126578445")
	um.add_provider_by_info("aa@gmail.com", "pwd", "smith", "john", 123, "GP")
	return um

@pytest.fixture
def cm_fixture(centre_fixture):
    cm = CentreManager()
    cm.add_centre(centre_fixture[0])
    cm.add_centre(centre_fixture[1])
    return cm

# @pytest.fixture
# def am_fixture():
# 	am = AppointmentManager()
# 	return am

# ****Valid date and time**** #

def test_past_date_and_time_slot():
	am = AppointmentManager()
	with pytest.raises(BookingError) as info:
		am.make_appt_and_add_appointment_to_manager('patient@gmail.com', 'prov@gmail.com', 'centre_id', '2016-08-09', '09:30', 'reason')


# test_non_existing_time_slot():

# test_valid_date_and_time_slot():


# ****Provider book with self**** #

# test_provider_book_with_self():


# ****Valid Booking**** #

# **Valid Provider and Centre** #

# test_non_existing_provider():

# test_non_existing_centre():

# test_existing_centre_and_provider():

# **Valid reason** #

# test_valid_reason():

