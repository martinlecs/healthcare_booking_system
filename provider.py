from user import User

class Provider(User):
	"Provider class"
	def __init__(self, email, password, surname, given_name, provider_no, service,
    centres=[], availability=[]):
		super().__init__(email, password)
		self._surname = surname
		self._given_name = given_name
		self._provider_no = provider_no
		self._service = service
		self._centres = centres
		self._availability = availability
		self._appointments = []
		self._rating = []

	@property
	def surname(self):
		return self._surname

	@property
	def given_name(self):
		return self._given_name

	@property
	def provider_no(self):
		return self._provider_no

	@property
	def service(self):
		return self._service

	@property
	def centres(self):
		return self._centres

	@property
	def availability(self):
		return self._availability

	@property
	def appointments(self):
		return self._appointments

	@property
	def rating(self):
		return self._rating

	@provider_no.setter
	def provider_no(self, provider_no):
		self._provider_no = provider_no

	@centres.setter
	def centres(self, centres):
		self._centres = centres

	@availability.setter
	def availability(self, availability):
		self._availability = availability

	# @appointments.setter
	# def appointments(self, appointments):
	# 	self._appointments = appointments

	# @rating.setter
	# def rating(self, rating):
	# 	self._rating = rating
	

	def view_current_appointments(self, appointment_id):
		curr_appt = []
		for appointment in self._appointments:
			if appointment.appointment_id == appointment_id:
				curr_appt.append(appointment)
		return curr_appt