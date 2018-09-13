import string
from patient import Patient
from provider import Provider

# use '.lower()' for service names
# Assumptions:
#	Service names passed in are correctly spelled and not not short hands (except GP)
#	All strings passed are all lower case


class UserManager:
	"User manager skeleton"
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

	# Given patient info, add it to patients list	
	def add_patient_by_info(self, email, password, surname, given_name, medicare_no):
		if not any(patient.email == email.lower() for patient in self._patients):
			self._patients.append(Patient(email, password, surname, given_name, medicare_no))
			return True		# Success, could instead return new patient object
		else:
			return False	# Failed (already in patients)
	
	# Given provider info, add it to providers list
	def add_provider_by_info(self, email, password, surname, given_name, provider_no, service):
		if not any(provider.email == email.lower() for provider in self._providers):
			self._providers.append(Provider(email, password, surname, given_name, provider_no, service))
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
	
	def search_by_patient_name(self, patient_name):
		# List of 'exact' match.
		# Creates a list of patient objects which contain the patient_name
		# substring in their surname or given_name attributes.
		# search_list = [match for match in self._patients if
		# 			   patient_name in match.surname
		# 			   or patient_name in match.given_name]
		#
		# Append 'near' matches to search list.
		# Or make own list?
		# near match search mechanism... speak to team about
		pass

	def search_by_provider_name(self, provider_name):
		# List of 'exact' match.
		# Creates a list of patient objects which contain the provider_name
		# substring in their surname or given_name attributes.
		# search_list = [match for match in self._providers if
		# 			   provider_name in match.surname
		# 			   or patient_name in match.given_name]
		#
		# Append 'near' matches to search list.
		# Or make own list?
		# near match search mechanism... speak to team about
		pass

	def search_by_service(self, service):
		if service.lower() in self._services.keys():
			return self._services[service.lower()]
		else:
			return False	# no service exists

	
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
	


'''
So our program needs to be able to read the csv file
	and from there get its patient, provider, centres
	and all other information.
I reached this conclusion from the response to my post on
	the assignment specs page: https://webcms3.cse.unsw.edu.au/COMP1531/18s2/resources/20423

So, when the information is read, it is passed to the user manager which instantiates objects.
So, when adding information, have to assume all info given is accurate, correct and spelled
	properly.
'''


'''
services dillema
Will services be of enum type? Is there a benefit to it?
Seem kind of restricted and look like it would just make things more complicated.
Should service names be strings?
When we have to implement registration, how will we take in new services?
Lets say we add a new service when providers register and say they provide a 
	service that isn't already on the system. What if this isn't a legit service?
	What if it's mispelled and added to the dictionary?
'''