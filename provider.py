from datetime import time, date
from user import User

class Provider(User):
	"Provider class"

	def __init__(self, email, password, surname, given_name,
	provider_no, service, appointments = [], availability = {}, rating = {}):
		super().__init__(email, password, surname, given_name, appointments)
		self._provider_no = provider_no
		self._service = service
		self._centres = centres
		self._availability = availability	#{centre_id:{date_obj:[time_slot]}}
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

	@property
	def average_rating(self):
		return self._average_rating
	

	@provider_no.setter
	def provider_no(self, provider_no):
		self._provider_no = provider_no

	@service.setter
	def service(self, service):
		self._service = service


	def add_centre(self, centre_name):
		centre_name = centre_name.lower()
		if centre_name not in self._centres:
			self._centres.append(centre_name)

	def remove_centre(self, centre_name):
		centre_name = centre_name.lower()
		if centre_name in self._centres:
			self._centres.remove(centre_name)

	def get_availability(self, centre_name, year, month, day):
		self.__add_date_to_centre_availability(centre_name.lower(), int(year), int(month), int(day))
		req_date = date(int(year), int(month), int(day))
		return self._availability[centre_name.lower()][req_date]
		# if centre_name.lower() not in self._availability.keys():
		# 	self.__add_centre_to_availability(centre_name)
		# if centre_name.lower() in availability.keys():
		# 	req_date = date(int(year), int(month), int(day))
		# 	if req_date not in self._availability[centre_name.lower()].keys():
		# 		self.__add_date_to_centre_availability(centre_name.lower(), int(year), int(month), int(day))
		# 	if req_date in self._availability[centre_name.lower()].keys():
		# 		return self._availability[centre_name.lower()][req_date]

	def __add_centre_to_availability(self, centre_name):
		if centre_name not in self._availability.keys():
			self._availability[centre_name] = {}

	def __add_date_to_centre_availability(self, centre_name, year, month, day):
		self.__add_centre_to_availability(centre_name)
		new_date = date(year, month, day)
		if new_date not in self._availability[centre_name].keys():
			free_time_slots = self.__make_time_slots_list()
			self._availability[centre_name][new_date] = free_time_slots

	def __make_time_slots_list(self):
		times = []
		times_string = []
		for hour in range(24):
			for minute in [00,30]:
				times.append(time(hour,minute))		
		for time_slots in times:
		    times_string.append(time_slots.strftime("%H:%M"))
		return times_string

	def make_time_slot_unavailable(self, centre_name, year, month, day, time_slot):
		centre_name = centre_name.lower()
		if centre_name in self._availability.keys():
			the_date = date(int(year), int(month), int(day))
			if the_date in self._availability[centre_name].keys():
				if time_slot in self._availability[centre_name][the_date]:
					self._availability[centre_name][the_date].remove(time_slot)

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
		if len(ratings) > 0:
			self._average_rating = sum(ratings)/float(len(ratings))
		else:
			self._average_rating = 0

''' # What I want to do

from datetime import time

times = []

for hour in range(24):
    for minute in [00,30]:
        times.append(time(hour,minute))

times_string = []

for time in times:
    times_string.append(time.strftime("%H:%M"))

'''