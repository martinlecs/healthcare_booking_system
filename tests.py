import pytest
from model.user_manager import UserManager
from model.centre_manager import CentreManager
from model.appointment_manager import AppointmentManager
from model.appointment import Appointment
from model.provider import Provider
from model.patient import Patient
from model.centre import Centre
from model.error import *
from model.notifications_manager import NotificationsManager
from model.permissions import Permissions
from datetime import datetime, date, time

''' 
Unit tests to run
Setup: Setup provider + user. Create appointments, present and past
Get appointments: Check returned appointments
Get past appointments: patient and provider
Check exceptions
    create second user:
    Access wrong appointment history: raise identity error
    Access specific appointment: raise identity error
    Appointment doesn't exist: Raise 404 error

Don't need to check incorrect or double booking, checked in different unit tests
'''

@pytest.fixture
def centres():
    cm = CentreManager.bootstrap()
    return [cm.centres[0], cm.centres[1]]

@pytest.fixture
def user_manager():
    um = UserManager.bootstrap()
    return um

@pytest.fixture
def appointment_manager():
    am = AppointmentManager()
    return am

@pytest.fixture
def patients(user_manager):
    p1 = user_manager.patients[0]
    p2 = user_manager.patients[1]
    return [p1, p2]

@pytest.fixture
def providers(user_manager):
    p1 = user_manager.providers[0]
    p2 = user_manager.providers[1]
    return [p1, p2]

@pytest.fixture
def appointments(appointment_manager, patients, providers, centres):
    c1 = centres[0]
    date1 = "2018-11-20"
    time1 = "13:00"
    time2 = "14:30"
    a1 = appointment_manager.make_appt_and_add_appointment_to_manager(patients[0].email, providers[0].email, c1,date1, time1, "")
    a2 = appointment_manager.make_appt_and_add_appointment_to_manager(patients[0].email, providers[1].email, c1,date1, time2, "")
    a3 = appointment_manager.make_appt_and_add_appointment_to_manager(patients[1].email, providers[0].email, c1,date1, time2, "")
    a4 = appointment_manager.make_appt_and_add_appointment_to_manager(patients[1].email, providers[0].email, c1,"2018-10-20", time2, "")
    a4._past = True
    return [a1, a2, a3, a4]

def test_current_appointment_number_patient(patients, providers, appointments, centres):
    p1 = patients[0]
    p1.add_appointment(appointments[0])
    p1.add_appointment(appointments[1])
    res = len(p1.get_upcoming_appointments())
    assert(res == 2)

def test_current_appointment_number_provider(patients, providers, appointments, centres):
    p1 = providers[0]
    p1.add_appointment(appointments[0])
    p1.add_appointment(appointments[2])
    res = len(p1.get_upcoming_appointments())
    assert(res == 2)

def test_past_appointment_number_patient(patients, providers, appointments, centres):
    p1 = patients[0]
    p1.add_appointment(appointments[0])
    p1.add_appointment(appointments[1])
    res = len(p1.get_upcoming_appointments())
    assert(res == 2)

def test_past_appointment_number_provider(patients, providers, appointments, centres):
    p1 = patients[0]
    p1.add_appointment(appointments[3])
    p1.add_appointment(appointments[0]) #add current to see it isn't counted
    res = len(p1.get_past_appointments())
    assert(res == 1)


def test_identity_error(patients):
    from model.system import correct_identity
    with pytest.raises(IdentityError) as error:
        correct_identity(patients[0], patients[1])



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


@pytest.fixture
def centre_fixture():
    c1 = Centre("Randwick Hospital", "Randwick","Hospital",1234,93000000)
    c2 = Centre("Prince of Wales", "Randwick", "Hospital", 1234, 93000000)
    c3 = Centre("Westmead Hospital", 1234, "Hospital", 1234, 93000000)
    c4 = Centre("Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    return [c1,c2,c3,c4]

@pytest.fixture
def prov_fixture():
    p1 = Provider("aa@gmail.com","pwd", "smith", "john", 123, "GP")
    p2 = Provider("bb@gmail.com","pwd","smith", "jane", 123, "GP")
    p3 = Provider("cc@gmail.com","pwd","sss", "jane", 123, "Physio")
    return [p1,p2,p3]

@pytest.fixture
def cm(centre_fixture):
    cm = CentreManager()
    cm.add_centre(centre_fixture[0])
    cm.add_centre(centre_fixture[1])
    return cm

def test_empty_list():
    cm = CentreManager()
    assert(len(cm.centres) == 0)

def test_add_centre(centre_fixture):
    cm = CentreManager()
    cm.add_centre(centre_fixture[0])
    assert(len(cm.centres) == 1)
    cm.add_centre(centre_fixture[1])
    assert(len(cm.centres) == 2)

def test_add_centre_dup(centre_fixture):
    cm = CentreManager()
    cm.add_centre(centre_fixture[0])
    cm.add_centre(centre_fixture[3])
    assert(len(cm.centres) == 1)

def test_add_invalid(centre_fixture):
    cm = CentreManager()
    invalid = centre_fixture[2]
    cm.add_centre(centre_fixture[0])
    cm.add_centre(invalid)
    assert(len(cm.centres) == 1)

def test_remove(cm, centre_fixture):
    cm.rem_centre(centre_fixture[0])
    assert(len(cm.centres) == 1)
    assert(centre_fixture[0] not in cm.centres)

def test_remove_by_name(cm):
    name = "Randwick Hospital"
    c = cm.rem_centre_by_name(name)
    assert(c not in cm.centres)
    assert(len(cm.centres) == 1)

def test_remove_duplicate(cm, centre_fixture):
    cm.rem_centre(centre_fixture[3])
    assert(len(cm.centres) == 1)
    assert(centre_fixture[0] not in cm.centres)

def test_remove_not_there(cm,centre_fixture):
    bef = cm.centres
    cm.rem_centre(centre_fixture[2])
    aft = cm.centres
    assert(bef is aft)

def test_remove_empty(centre_fixture):
    cm = CentreManager()
    res = cm.rem_centre(centre_fixture[0])
    assert(res == False)

def test_add_from_details(prov_fixture):
    cm = CentreManager()
    cm.add_centre_from_details("Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    cm.add_centre_from_details(
        "Prince of Wales", "Randwick", "Hospital", 1234, 93000000)
    assert(len(cm.centres) == 2)

def test_add_from_details_duplicate(cm, centre_fixture):
    bef = len(cm.centres)
    res = cm.add_centre_from_details(
        "Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    aft = len(cm.centres)
    assert(bef == aft)
    assert(res == False)

def test_add_from_invalid_details(cm):
    res = cm.add_centre_from_details(
        "Randwick Hospital", 1234, "Hospital", 1234, 93000000)
    assert(res == False)
    assert(len(cm.centres) == 2)


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


def test_getters():
    p = Provider('test@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')
    info = p.get_information()
    assert(info["email"] == 'test@gmail.com'.lower())
    assert(info["password"]	== '1234'.lower())
    assert(info["surname"] 	== 'McTester'.lower())
    assert(info["given_name"] == 'Test'.lower())
    assert(info["provider_no"] == '124024114'.lower())
    assert(info["service"] == 'Official Tester'.lower())
    assert(info["appointments"] == [])
    assert(info["centres"] == [])
    assert(info["availability"] == {})
    assert(info["rating"] == 0)

def test_setters():
    p = Provider('test@gmail.com','1234','McTester', 'Test','124024114', 'Official Tester')

    p.email = 'TESting@gmail.Com'
    info = p.get_information()
    assert(info['email'] == 'testing@gmail.com' )

    p.password = 'WoooWThatsGreat'
    info = p.get_information()
    assert(info['password'] != 'wooowthatsgreat' and info['password'] == 'WoooWThatsGreat')

    p.surname = 'MCTESTing'
    info = p.get_information()
    assert(info['surname'] == 'mctesting')

    p.given_name = 'TEEEESt'
    info = p.get_information()
    assert(info['given_name'] == 'teeeest')

    p.provider_no = '123123'
    info = p.get_information()
    assert(info['provider_no'] == '123123')

    p.service = 'OFFicial TESTer'
    info = p.get_information()
    assert(info['service'] == 'official tester')


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

def test_get_availability_invalid_date():
    p = Provider('1','1','1','','','')
    with pytest.raises(DateTimeValidityError) as info:
        checker = p.get_availability('centre', 13, 22, 414)
    with pytest.raises(DateTimeValidityError) as info:
        checker = p.get_availability('centre', 'lol', 22, 414)


def test_get_availability_for_non_existing_centre_but_valid_date():
    p = Provider('1','1','1','','','')
    # p.add_centre('rand')
    with pytest.raises(BookingError) as info:
        p.get_availability('centre', 2019, 12, 14)

def test_get_availability_for_existing_centre_and_valid_date():
    p = Provider('1','1','1','','','')
    p.add_centre('rand')
    with pytest.raises(DateTimeValidityError) as info:
        checker = p.get_availability('rand', 2018, 19, 220)


def test_make_non_existing_and_available_slots_unavailable():
    p = Provider('1','1','1','','','')
    p.add_centre('rand')
    p.get_availability('rand', 2019, 9, 20)
    checker = p.make_time_slot_unavailable('rand', 2019, 9, 20, '08:30')
    assert(checker == True)
    val = p.get_availability('rand', 2019, 9, 20)
    assert('08:30' not in val)
    checker = p.make_time_slot_unavailable('rand', 2019, 9, 20, '09:30')
    val = p.get_availability('rand', 2019, 9, 20)
    assert('08:30' not in val and '09:30' not in val)

def test_get_availability_for_existing_date():
    p = Provider('1','1','1','','','')
    p.add_centre('rand')
    p.get_availability('rand', 2019, 9, 20)
    p.make_time_slot_unavailable('rand', 2019, 9, 20, '08:30')
    val = p.get_availability('rand', 2019, 9, 20)
    assert('08:30' not in val and type(val) is list)


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
    assert(um.get_service_names() == ['gp'])
    assert(um.services['gp'] == ['example@gmail.com'])
    um.add_provider_by_info('exaample2@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'Prac')
    assert(um.get_service_names() == ['gp', 'prac'])
    assert(um.services['prac'] == ['exaample2@gmail.com'])

# test new provider added to existing dict
def test_new_provider_to_existing_service():
    um = UserManager()
    um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
    um.add_provider_by_info('example2@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
    assert(um.get_service_names() == ['gp'])
    assert(um.services['gp'] == ['example@gmail.com', 'example2@gmail.com'])


# Test get service names
def test_get_service_names():
    um = UserManager()
    um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'GP')
    assert(um.get_service_names() == ['gp'])
    um.add_provider_by_info('exaample2@gmail.com', 'password', 'Cena', 'John', '04253634223' ,'Prac')
    assert(um.get_service_names() == ['gp', 'prac'])

# test get existing user
def test_get_existing_user():
    um = UserManager()
    um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '02141244235' ,'GP')
    um.add_provider_by_info('example2222@gmail.com', 'password', 'Cena', 'John', '02141244235' ,'GP')
    p1 = um.get_user('example@gmail.com')
    assert(p1 is not None)
    assert(p1.email == 'example@gmail.com')
    assert(p1.password == 'password')

# test get non-existing user
def test_get_non_existing_user():
    um = UserManager()
    um.add_provider_by_info('example@gmail.com', 'password', 'Cena', 'John', '02141244235' ,'GP')
    um.add_provider_by_info('example2222@gmail.com', 'password', 'Cena', 'John', '02141244235' ,'GP')
    with pytest.raises(IdentityError) as error:
        p1 = um.get_user('exampl23123e@gmail.com')


# test removing existing from patients
def test_remove_existing_patient():
    um = UserManager()
    um.add_patient_by_info('example@gmail.com', 'password', 'Cena', 'John', '04253634223')
    assert(len(um.patients) == 1 )
    assert(um.patients[0].email == 'example@gmail.com')
    assert(um.get_user('example@gmail.com') is not None)
    assert(um.remove_patient('example@gmail.com'))
    assert(um.patients == [])
    assert(um.get_service_names() == [])

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
    assert(um.get_user('example@gmail.com') is not None)
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


''' 
Items to test
Search Providers
    Search all
    Search by name full
    Search by name prefix
    Search by name suffix
    Search by name substring
    Search by name larger
    Search by name thats not there
**** Done up to here ****
    Search by suburb
    Search by suburb thats not there
    Search with invalid input (i.e integer)
'''


@pytest.fixture
def prov_fixture1():
    p1 = Provider("aa@gmail.com", "pwd", "smith", "john", 123, "GP")
    p2 = Provider("bb@gmail.com", "pwd", "smith", "jane", 123, "Surgeon")
    p3 = Provider("cc@gmail.com", "pwd", "sss", "jane", 123, "Physio")
    p4 = Provider("dd@gmail.com", "pwd", "Strange", "Stephen", 123, "GP")
    return [p1, p2, p3, p4]


@pytest.fixture
def centre_fixture1():
    c1 = Centre("Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    c2 = Centre("Prince of Wales", "Randwick", "Hospital", 1234, 93000000)
    c3 = Centre("Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    return [c1, c2, c3]


@pytest.fixture
def um(prov_fixture1, centre_fixture1):
    um = UserManager()
    um.add_provider_by_info("aa@gmail.com", "pwd", "smith", "john", 123, "GP")
    um.add_provider_by_info("bb@gmail.com", "pwd", "smith", "jane", 123, "Surgeon")
    um.add_provider_by_info("cc@gmail.com", "pwd", "sss", "jane", 123, "Physio")
    um.add_provider_by_info("dd@gmail.com", "pwd", "Strange", "Stephen", 123, "GP")
    return um



def test_provider_search_all_name(um):
    result = um.search_name("")
    assert(result == um.providers)


def test_provider_search_first_name_exact(um):
    text = "jane"
    result = um.search_name(text)
    assert(result != [])
    for i in result:
        assert(text == i.given_name)

def test_provider_search_last_name_exact(um):
    text = "smith"
    result = um.search_name(text)
    assert(len(result)==2)
    for i in result:
        assert(text == i.surname)

def test_provider_search_both_name_exact(um):
    text = "jane smith"
    result = um.search_name(text)
    assert(len(result) == 1)
    for i in result:
        print(i.email)

def test_provider_search_name_prefix(um):
    text = "Step"
    result = um.search_name(text)
    assert(len(result) == 1)
    for i in result:
        assert(text.lower() in i.given_name)

def test_provider_search_name_insensitive(um):
    text = "SmITh"
    result = um.search_name(text)
    assert(result != [])
    for i in result:
        assert(text.lower() in i.surname.lower())


def test_provider_search_name_suffix(um):
    text = "phen"
    result = um.search_name(text)
    assert(result == [])


def test_provider_search_name_wrong(um):
    text = "Tim"
    result = um.search_name(text)
    assert(result == [])

def test_service_all(um):
    result = um.search_service("")
    assert(result == um.providers)

def test_provider_search_service_exact(um):
    text = "gp"
    result = um.search_service(text)
    assert(len(result) == 2)


''' 
Items to test
Search Centres
    Search all
    Search by name full
    Search by name prefix
    Search by name suffix
    Search by name substring
    Search by name larger
    Search by name thats not there
**** Done up to here ****
    Search by suburb
    Search by suburb thats not there
    Search with invalid input (i.e integer)
'''

@pytest.fixture
def prov_fixture2():
    p1 = Provider("aa@gmail.com", "pwd", "smith", "john", 123, "GP")
    p2 = Provider("bb@gmail.com", "pwd", "smith", "jane", 123, "GP")
    p3 = Provider("cc@gmail.com", "pwd", "sss", "jane", 123, "Physio")
    return [p1, p2, p3]

@pytest.fixture
def cm2(prov_fixture2):
    cm = CentreManager()
    c1 = Centre("Randwick Hospital", "Randwick", "Hospital",1234,93000000)
    c2 = Centre("Prince of Wales", "Randwick", "Hospital",1234,93000000)
    c3 = Centre("Randwick Hospital", "Randwick", "Hospital", 1234, 93000000)
    c3.add_provider(prov_fixture2[0])
    c3.add_provider(prov_fixture2[2])
    c4 = Centre("RPA", "Camperdown", "Hospital", 1234, 93000000)
    c4.add_provider(prov_fixture2[0])
    c4.add_provider(prov_fixture2[1])
    c4.add_provider(prov_fixture2[2])
    for centre in [c1,c2,c3,c4]:
        cm.add_centre(centre)
    return cm

def test_centre_search_all_name(cm2):
    result = cm2.search_name("")
    assert(result == cm2.centres)

def test_centre_search_all_suburb(cm2):
    result = cm2.search_suburb("")
    assert(result == cm2.centres)

def test_centre_search_name_exact(cm2, ):
    text = "Randwick Hospital"
    result = cm2.search_name(text)
    for i in result:
        assert(text == i.name)

def test_centre_search_name_prefix(cm2):
    text = "Rand"
    result = cm2.search_name(text)
    for i in result:
        assert(text in i.name)

def test_centre_search_name_insensitive(cm2):
    text = "rAnDwick"
    result = cm2.search_name(text)
    assert(result != [])
    for i in result:
        assert(text.lower() in i.name.lower())

def test_centre_search_name_suffix(cm2):
    text = "wick"
    result = cm2.search_name(text)
    assert(result == [])

def test_centre_search_name_wrong(cm2):
    text = "Royal"
    result = cm2.search_name(text)
    assert(result == [])

def test_centre_serach_name_longer(cm2):
    text = "RPAA"
    result = cm2.search_name(text)
    for i in result:
        assert(i.name.lower() in text.lower())

def test_centre_search_all_suburb(cm2):
    result = cm2.search_suburb("")
    assert(result == cm2.centres)


def test_centre_search_suburb_exact(cm2):
    text = "Camperdown"
    result = cm2.search_suburb(text)
    for i in result:
        assert(text == i.suburb)

def test_centre_search_suburb_prefix(cm2):
    text = "Rand"
    result = cm2.search_suburb(text)
    for i in result:
        assert(text in i.suburb)

def test_centre_search_suburb_insensitive(cm2):
    text = "cAmPerDOWN"
    result = cm2.search_suburb(text)
    assert(result != [])
    for i in result:
        assert(text.lower() in i.suburb.lower())


def test_centre_search_suburb_suffix(cm2):
    text = "wick"
    result = cm2.search_suburb(text)
    assert(result == [])


def test_centre_search_suburb_wrong(cm):
    text = "Parramatta"
    result = cm.search_suburb(text)
    assert(result == [])
