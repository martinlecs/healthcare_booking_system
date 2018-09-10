from flask_login import UserMixin

class User(UserMixin):
	"User class"
	def __init__(self, email, password, surname, given_name, appointments=[]):
		self._email = email
		self._password = password
		self._surname = surname
		self._given_name = given_name
		self._appointments = appointments

	@property
	def email(self):
		return self._email
	
	@property
	def password(self):
		return self._password

	@property
	def surname(self):
		return self._surname
	
	@property
	def given_name(self):
		return self._given_name

	@property
	def appointments(self):
		return self._appointments
	

	@email.setter
	def email(self, email):
		self._email = email

	@password.setter
	def password(self, pwd):
		self._password = pwd

	@surname.setter
	def surname(self, surname):
		self._surname = surname

	@given_name.setter
	def given_name(self, given_name):
		self._given_name = given_name

	def add_appointment(self, appointment_id):
		if appointment_id is not in self._appointments:
			self._appointments.append(appointment_id)

	def remove_appointment(self, appointment_id):
		if appointment_id is in self._appointments:
			self._appointments.remove(appointment_id)

	def get_id(self):
		return self._email
