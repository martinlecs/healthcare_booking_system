from patient import Patient
from provider import Provider


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
	# Redundent if service names will be enum
	# If service is enum, can return 'available services'
	#	which refers to services which are associated with a
	#	provider
	def get_service_names(self):
		return [*self._services]	# returns list of services

	def get_patient(self, email):
		for patient in self._patients:
			if patient.email = email:
				return patient

	def get_provider(self, email):
		for provider in self._providers:
			if provider.email = email:
				return provider
	

	# Given patient info, add it to patients list	
	def add_patient_by_info(self, email, password, surname, given_name, medicare_no):
		if not any(patient.email == patient_email for patient in self._patients):
			patient = Patient(email, password, surename, given_name, medicare_no)
			self._providers.append(patient)
			return True	# Success, could instead return new patient object
		else:
			return False	# Failed (already in patients)

	# # Given patient object, add to patients
	# # Less recommended
	# def add_patient(self, patient):
	# 	if patient not in self._patients:	
	# 		self._patients.append(patient)
	# 		return True 	# Success, could instead return new patient object
	# 	else:
	# 		return False	# Failed (already in patients)
	
	# Given provider info, add it to providers list
	def add_provider_by_info(self, email, password, surname, given_name, provider_no, service):
		if not any(provider.email == provider_email for provider in self._providers):
			provider = provider(email, password, surename, given_name, provider_no, service)
			self._providers.append(provider)
			self.__add_provider_to_services(email, service)
			return True		# Success, could instead return new provider object
		else:
			return False	# Failed (already in providers)


	# # Given provider object, add to providers
	# # Less recommended
	# def add_provider(self, provider):
	# 	if provider not in self._providers:	
	# 		self._providers.append(provider)
	# 		return True		# Success
	# 	else:
	# 		return False	# Failed (already in providers)

	def remove_patient(self, patient_email):
		for i, patient in self._patients:
			if patient.email == patient_email:
				del self._patients[i]
				return True
		return False

	def remove_provider(self, provider_email):
		for i, provider in self._providers:
			if provider.email == provider_email:
				del self._providers[i]
				self.__remove_provider_from_services(provider_name)
				return True
		return False

		# or
		'''
		for provider in self._providers:
			if provider.email == provider_email:
				del self._providers[i]
				return True
		'''
	
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
		if service in self._services.keys():
			return self._services[service]
		else:
			return False	# no service exists

	## Helper Functions ##
	def __add_provider_to_services(self, email, service):
		if service is in self._services.keys():
			if email not in self._services[service]:
				self._services[service].append(service)
		else:
			self._services[services] = [email]

	def __remove_provider_from_services(self, email):
		for service in self._services.keys():
			if email in self._services[service]:
				self._services[service].remove(email)
				break

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