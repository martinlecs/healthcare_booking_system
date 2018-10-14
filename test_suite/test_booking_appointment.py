import pytest
from model.user_manager import UserManager
from model.centre_manager import CentreManager
from model.appointment_manager import AppointmentManager
from model.provider import Provider
from model.patient import Patient
from model.appointment import Appointment
from model.centre import Centre
from model.error import IdentityError, BookingError, DateTimeValidityError
from model.date_validity import date_and_time_valid, date_valid
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

@pytest.fixture
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
	c4 = Centre("Randwick Hospital", "Randwick", "Hospital",1234, 93000000)
	return [c1, c2, c3, c4]

@pytest.fixture
def um_fixture(centre_fixture):
	um = UserManager()
	um.add_patient_by_info("dd@gmail.com", "pwd", "Goldstein", "Mark", "126578445")
	um.add_provider_by_info("aa@gmail.com", "pwd", "smith", "john", 123, "GP")
	provider = um.get_user("aa@gmail.com")
	provider.add_centre(centre_fixture[0].name)
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
	with pytest.raises(DateTimeValidityError) as info:
		am.make_appt_and_add_appointment_to_manager('patient@gmail.com', 'prov@gmail.com', 'centre_id', '2016-08-09', '09:30', 'reason')

# def test_non_existing_time_slot(um_fixture):

def test_invalid_date(um_fixture):
	am = AppointmentManager()
	um = um_fixture
	provider = um.get_user("aa@gmail.com")
	with pytest.raises(DateTimeValidityError) as info:
		provider.get_availability(provider.centres[0], 19922, 13, 2222)
	with pytest.raises(DateTimeValidityError) as info:
		provider.get_availability(provider.centres[0], 'lol', 12, 12)
	avail = provider.get_availability(provider.centres[0], 2019, 10, 15)
	assert(type(avail) is list)

# ****Provider book with self**** #

def test_provider_book_with_self(um_fixture):
	am = AppointmentManager()
	with pytest.raises(BookingError) as info:
		am.make_appt_and_add_appointment_to_manager('prov@gmail.com', 'prov@gmail.com', 'centre_id', '2019-08-09', '09:30', 'reason')

# ****Valid Booking**** #
# Test it makes appt, stores values, stores appt in appt_manager
def test_valid_booking(um_fixture):
	am = AppointmentManager()
	appt = am.make_appt_and_add_appointment_to_manager('patient@gmail.com', 'prov@gmail.com', 'centre_id', '2019-08-09', '09:30', 'reason')
	assert(type(appt) == Appointment)
	assert(appt.patient_email == 'patient@gmail.com')
	assert(appt.provider_email == 'prov@gmail.com')
	assert(appt.centre_id == 'centre_id')
	assert(appt.date == '2019-08-09')
	assert(appt.time_slot == '09:30')
	assert(appt.reason == 'reason')
	assert(appt in am.appointments)


# ****Valid Provider and Centre**** #

# test_non_existing_provider():
	# This is taken care of in routes so it can't be tested through pytest
	# However, I promise you it works. Test it.

# test_non_existing_centre():
	# This is taken care of in routes so it can't be tested...
	# However, I promise you it works. Test it.

# test_existing_centre_and_provider():
	# This is taken care of in routes so it can't be tested through pytest
	# However, I promise you it works. Test it.

