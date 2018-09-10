from user import User

class Patient(User):
	"Patient class"
	def __init__(self, email, password, surname, given_name, appointments, medicare_no):
		super().__init__(email, password, surname, given_name, appointments)
		self._medicare_no = medicare_no

	@property
	def medicare_no(self):
		return self._medicare_no

	@medicare_no.setter
	def medicare_no(self, medicare_no):
		self._medicare_no = medicare_no

	def view_past_appointments(self):
		past_appointments = []
		for appt in appointments:
			if appt.past == true:
				past_appointments.append(appt)
		return past_appointments

	def view_current_appointments(self):
		cur_appointments = []
		for appt in appointments:
			if appt.past == false:
				cur_appointments.append(appt)
		return cur_appointments
