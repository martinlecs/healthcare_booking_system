from user import User

class Provider(User):
	"Provider class"
	def __init__(self, email, password, surname, given_name,
				provider_no, service, centres = [], appointments = [], availability = {}, rating = {}):
		super().__init__(email, password, surname, given_name, appointments)
		self._provider_no = provider_no
		self._service = service
		self._centres = centres
		self._availability = availability	#{centre_id:{date:[time_slot]}}	time_slot
		# self._rating = {}
		self._average_rating = 0

	@property
	def provider_no(self):
		return self._provider_no

	@property
	def fullname(self):
		return " ".join([self._given_name, self._surname])

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
	def rating(self):
		return self._average_rating

	@provider_no.setter
	def provider_no(self, provider_no):
		self._provider_no = provider_no

	@service.setter
	def service(self, service):
		self._service = service

	def get_information(self):
		return { 'email': self.email,
				 'surname': self.surname,
				 'given_name': self.given_name,
				 'provider_no': self._provider_no,
				 'service': self._service,
				 'centres': self._centres,
				 'appointments': self.appointments,
				 'availability': self._availability,
				 'rating': self._average_rating,
				}


	def add_centres(self, centre):
		if centre not in self._centres:
			self._centres.append(centre)

	def rem_centre(self, centre_name):
		if centre_name in self._centres:
			self._centres.remove(centre_name)

	
	# def make_time_slot_unavailable(self, date, time_slot):
	# 	pass

	# check_if_time_slot_available(self, time_slot):
	#	pass

	# add rating to dict, recalculate average rating
	def add_rating(self, patient_email, rating):
		self._rating[patient_email] = rating
		self.__calc_average_rating()

	# pop rating from dictionary
	def remove_rating(self, patient_email):
		self._rating.pop(patient_email, None)

	# private function to recalculate average rating
	def __calc_average_rating(self):
		ratings = list(self._rating.values())
		self._average_rating = sum(ratings)/float(len(ratings))
