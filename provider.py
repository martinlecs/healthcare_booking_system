from datetime import time, date
from user import User

# Note about availability at the bottom
# 

class Provider(User):
	"Provider class"
	def __init__(self, email, password, surname, given_name,provider_no, service):
		super().__init__(email, password, surname, given_name)
		self._provider_no = provider_no.lower()
		self._service = service.lower()
		self._centres = [] #centres
		self._availability = {} #availability	#{centre_id:{date:[time_slot]}}
		self._rating = {} #rating
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
		self._provider_no = provider_no.lower()

	@service.setter
	def service(self, service):
		self._service = service.lower()


	def add_centre(self, centre_name):
		centre_name = centre_name.lower()
		if centre_name not in self._centres:
			self._centres.append(centre_name)

	def remove_centre(self, centre_name):
		centre_name = centre_name.lower()
		if centre_name in self._centres:
			self._centres.remove(centre_name)
			return True
		return False

	# Returns available time slots 
	def get_availability(self, centre_name, year, month, day):
		centre_name = centre_name.lower()
		if centre_name in self._centres:
			req_date = date(int(year), int(month), int(day))
			if req_date in self._availability[centre_name]:
				return self._availability[centre_name][req_date]
			else:
				return self.__make_time_slots_list() # Default slots as if they exist and then add date & time slots later
		else:
			return False	# ERROR, centre doesn't exist or centre isn't in provider's centes attribute

	# Removes time slot from availability. If time slot and date don't exist, add them, 
	# 	then remove time slot
	def make_time_slot_unavailable(self, centre_name, year, month, day, time_slot):
		centre_name = centre_name.lower()
		if centre_name.lower() in self._centres:
			new_date = date(int(year), int(month), int(day))
			if new_date not in self._availability[centre_name].keys():
				free_time_slots = self.__make_time_slots_list()
				self._availability[centre_name][new_date] = free_time_slots
				if time_slot not in free_time_slots:
					return False	# ERROR
			self._availability[centre_name][new_date].remove(time_slot)
			return True
		else:
			False	# ERROR

	# Makes a list of 48 strings representing 30 mins time slots, of 24 hours  
	def __make_time_slots_list(self):
		times = []
		times_string = []
		for hour in range(24):
			for minute in [00,30]:
				times.append(time(hour,minute))		
		for time_slots in times:
		    times_string.append(time_slots.strftime("%H:%M"))
		return times_string

	
	# add rating to dict, recalculate average rating
	def add_rating(self, patient_email, rating):
		self._rating[patient_email] = rating
		self.__calc_average_rating()

	# pop rating from dictionary
	def remove_rating(self, patient_email):
		self._rating.pop(patient_email, None)
		self.__calc_average_rating()

	# private function to recalculate average rating
	def __calc_average_rating(self):
		ratings = list(self._rating.values())
		if len(ratings) > 0:
			self._average_rating = sum(ratings)/float(len(ratings))
		else:
			self._average_rating = 0


# Important note about availability:
'''
As can been seen by the comment next to the availability attribute,
availability is a dictionary that associates a centre with working hours.
{centre_id:{date:[time_slot]}}

Working hours is as a dictionary that associates a date with a list of time slots
in the form of strings. E.g a possible time slot = '09:00 - 09:30'

In the booking form, a date is selected, get_availability() is called and the available times for that date
is returned.

Get_availability() has two possible returns:
	1. A list of time slots associated with a date and centre
	2. A default list of time slots, for the case when the
	   date selected isn't associated with a health centre

A date becomes associated (added to the health care's dictionary) when a patient
books an appointment on that date. 

So until the time is booked, the default list is returned and shown on the website, which is a list containing all
time slots partitioning 24 hours into 30mins.
'''