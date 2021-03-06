import string
from model.patient import Patient
from model.provider import Provider
from model.error import IdentityError
import csv
import pickle

# use '.lower()' for service names
# Assumptions:
#	Service names passed in are correctly spelled and not not short hands (except GP)
#	All strings passed are all lower case


class UserManager:
	''' User Manager Class '''
	def __init__(self):
		self._patients = []
		self._providers = []
		self._services = {}	# {service<string>: [provider_emails<string>]}

	#Getters
	@property
	def patients(self):
		return self._patients
	
	@property
	def providers(self):
		return self._providers

	@property
	def services(self):
		return self._services

	def specialists(self):
		spec = []
		for p in self.providers:
			if p.specialist is True:
				spec.append(p)
		return spec

	# Returns List of service names
	def get_service_names(self):
		return [*self._services]

	def get_user(self, email):
		user = self.__get_patient(email.lower())
		if user is not None:
			return user
		user = self.__get_provider(email.lower())
		if user is not None:
			return user
		raise IdentityError("User doesn't exist")

	# Given patient info, add it to patients list
	def add_patient_by_info(self, email, password, surname, given_name, medicare_no):
		if not any(patient.email == email.lower() for patient in self._patients):
			self._patients.append(Patient(email, password, surname, given_name, medicare_no))
			return True		# Success, could instead return new patient object
		else:
			return False	# Failed (already in patients)
	
	# Given provider info, add it to providers list
	def add_provider_by_info(self, email, password, surname, given_name, provider_no, service, specialist=False):
		if not any(provider.email == email.lower() for provider in self._providers):
			self._providers.append(Provider(email, password, surname, given_name, provider_no, service, specialist))
			self.__add_provider_to_services(email.lower(), service.lower())
			return True		# Success, could instead return new provider object
		else:
			return False	# Failed (already in providers)


	def remove_patient(self, patient_email):
		for i, patient in enumerate(self._patients):
			if patient.email == patient_email.lower():
				del self._patients[i]
				return True
		return False

	def remove_provider(self, provider_email):
		for i, provider in enumerate(self._providers):
			if provider.email == provider_email.lower():
				del self._providers[i]
				self.__remove_provider_from_services(provider_email.lower())
				return True
		return False

	def is_valid_user(self, email, password):
		user = self.get_user(email.lower())
		if user is not None:
			if user.password == password:
				return user
	

	#Searches providers by first name or last name. Returns list of providers
	#Adds prefix match for first or last as well
	def search_name(self, search):
		#First need to handle search term if its 1 or 2 words
		if search == "":
			return self._providers
		names = search.lower().split()
		if len(names) > 1:
			return self.search_full_name(names)
		else:
			providers = []
			for provider in self._providers:
				first = provider.given_name.lower()
				last = provider.surname.lower()
				if ((names[0] in first) and names[0][0] is first[0]) or ((names[0] in last) and names[0][0] is last[0]):
					providers.append(provider)
			return providers

	# If they put in two names, matches first AND last name
	#prefix match to both applies so joh smit = john smith
	def search_full_name(self, names):
		providers = []
		for provider in self._providers:
			first = provider.given_name.lower()
			last = provider.surname.lower()
			if ((names[0] in first) and names[0][0] is first[0]) and ((names[1] in last) and names[1][0] is last[0]):
				providers.append(provider)
		return providers

	#Dictionary allows quick access to list of providers, but only emails
	#instead of searching in the flask app, convert emails to objects in the
	# function instead and return list of providers
	def search_service(self, service):
		providers = []
		if service == "":
			return self.providers
		if service in self._services.keys():
			emails = self._services[service]
			for e in emails:
				providers.append(self.get_user(e))
			return providers
		else:
			return False  # no service exists

	
	## Helper Functions ##
	def __add_provider_to_services(self, email, service):
		if service in self._services.keys():
			if email not in self._services[service]:
				self._services[service].append(email)
		else:
			self._services[service] = [email]

	def __remove_provider_from_services(self, email):
		for service in self._services.keys():
			if email in self._services[service]:
				self._services[service].remove(email)
				break

	def __get_patient(self, email):
		for patient in self._patients:
			if patient.email == email:
				return patient

	def __get_provider(self, email):
		for provider in self._providers:
			if provider.email == email:
				return provider

	def get_provider(self, email):
		for provider in self._providers:
			if provider.email == email:
				return provider
		return None
	"""  
	Load/Save Data methods:
	load_data checks if there is a pickle file for the users (currently only implemented providers)
	if it does, loads that and returns user manager object, otherwise opens the csv and extracts data
	bootstrap is the init function on 'startup' that performs this
	"""
	def save_data(self):
		with open('model/data/users.dat', 'wb') as file:
			pickle.dump(self, file)

	@classmethod
	def load_data(cls):
		try:
			with open('model/data/users.dat', 'rb') as file:
				user_manager = pickle.load(file)
		except IOError:
			user_manager = UserManager.bootstrap()
		return user_manager

	@classmethod
	def bootstrap(cls):
		um = UserManager()
		with open('model/data/provider.csv', newline='') as file:
			reader = csv.reader(file, dialect='excel', quotechar="'")
			for row in reader:
				email = row[0].strip()
				pwd = row[1].strip()
				name = row[0].strip().split('@')[0]
				surname = ""
				no = 0
				service = row[2].strip()
				um.add_provider_by_info(email, pwd, surname, name, no, service)
				#Need to insert error handling
		with open('model/data/specialist.csv', newline='') as file:
			reader = csv.reader(file, dialect='excel', quotechar="'")
			for row in reader:
				email = row[0].strip()
				pwd = row[1].strip()
				name = row[0].strip().split('@')[0]
				surname = ""
				no = 0
				service = row[2].strip()
				um.add_provider_by_info(email, pwd, surname, name, no, service, True)
		with open('model/data/patient.csv', newline='') as file:
			reader = csv.reader(file, dialect='excel', quotechar="'")
			for row in reader:
				email = row[0].strip()
				pwd = row[1].strip()
				name = row[0].strip().split('@')[0]
				surname = ""
				medicare_no = 0
				um.add_patient_by_info(email, pwd, surname, name, medicare_no)
		with open('model/data/provider_health_centre.csv', newline='') as file:
			reader = csv.reader(file, dialect='excel', quotechar="'")
			for row in reader:
				prov_email = row[0].strip()
				centre_name = row[1].strip()
				for provider in um.providers:
					if provider.email.lower() == prov_email.lower():
						provider.add_centre(centre_name)
						break
				#Need to insert error handling
		return um



'''
******* NOTES FOR SEARCH ** *******
May need to return provider object instead of just email in case we need to access the attributes
Will check once front end is implemeneted

Search can either be done by a single name, which searches first or last name, or both
Still does prefix match for all
'''