from user import User
from appointment import Appointment

class Patient(User):
	"Patient class"
	def __init__(self, email, password, surname, given_name, medicare_no, appointments=[]):
		super().__init__(email, password)
		self._surname = surname
		self._given_name = given_name
		self._medicare_no = medicare_no
		self._appointments = appointments

	@property
	def surname(self):
		return self._surname

	@property
	def given_name(self):
		return self._given_name

	@property
	def medicare_no(self):
		return self._medicare_no

	@property
	def appointments(self):
		return self._appointments

	@medicare_no.setter
	def medicare_no(self, medicare_no):
		self._medicare_no = medicare_no

	@appointments.setter
	def appointments(self, appointments):
		self._appointments = appointments

	def view_current_appointments(self, appointment_id):
		curr_appt = []
		for appointment in self._appointments:
			if appointment.appointment_id == appointment_id:
				curr_appt.append(appointment)
		return curr_appt