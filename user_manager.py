from patient import Patient
from provider import Provider


class UserManager:
	"User manager skeleton"
	def __init__(self):
		self._patients = []
		self._providers = []
		self._services = {}	# {service<enum>: [provider_emails]}

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

	def get_services(self):
		return [*self._services]	# returns list of services
	

	# Given patient info, add it to patients list	
	def add_patient_by_info(self, email, password, surname, given_name, medicare_no):
		if not any(patient.email == patient_email for patient in self._patients):
			patient = Patient(email, password, surename, given_name, medicare_no)
			self._providers.append(patient)
			return True	# Success, could instead return new patient object
		else:
			return False	# Failed (already in patients)

	# Given patient object, add to patients
	# Less recommended
	def add_patient(self, patient):
		if patient not in self._patients:	
			self._patients.append(patient)
			return True 	# Success, could instead return new patient object
		else:
			return False	# Failed (already in patients)
	
	# Given provider info, add it to providers list
	def add_provider_by_info(self, email, password, surname, given_name, provider_no, service):
		if not any(provider.email == provider_email for provider in self._providers):
			provider = provider(email, password, surename, given_name, provider_no, service)
			self._providers.append(provider)
			return True		# Success, could instead return new provider object
		else:
			return False	# Failed (already in providers)
	
	# Given provider object, add to providers
	# Less recommended
	def add_provider(self, provider):
		if provider not in self._providers:	
			self._providers.append(provider)
			return True		# Success
		else:
			return False	# Failed (already in providers)

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
				return True
		return False
	
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
		return self._services['service']


