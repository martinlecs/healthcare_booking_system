from user import User

class Provider(User):
	"Provider class"
	def __init__(self, email, password, surname, given_name,
	provider_no, service, appointments = [], availability = {}, rating = {}):
		super().__init__(email, password, surname, given_name, appointments)
		self._provider_no = provider_no
		self._service = service
		self._centres = centres
		self._availability = availability	#{centre_id:{date:[time_slot]}}	time_slot
		self._rating = {}
		self._average_rating = 0

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
	def rating(self):
		return self._rating

	@provider_no.setter
	def provider_no(self, provider_no):
		self._provider_no = provider_no

	@service.setter
	def service(self, service):
		self._service = service


	def add_centre(self, centre):
		if centre not in self._centres:
			self._centres.append(centre)

	def remove_centre(self, centre_name):
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
		self._rating.pop(patient_email, none)
		self.__calc_average_rating()

	# private function to recalculate average rating
	def __calc_average_rating(self):
		ratings = list(self._rating.values())
		self._average_rating = sum(ratings)/float(len(ratings))
