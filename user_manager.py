from patient import Patient
from provider import Provider


class UserManager:
	"User manager skeleton"
	def __init__(self):
		self._patients = []
		self._providers = []

	#Getters
	@property
	def patients(self):
		return self._patients
	
	@property
	def providers(self):
		return self._providers

	# Pass in a patient object and it gets added.
	# instead, (maybe) gonna have patient info passed through
	#  and add_patient makes the class instance and addes
	#  the object to patients list instead.
	# e.g.:
	# If new patient info doesn't exist in self._patients
	#  then make new patient instance and add to self._patients
	# Should return new patient object, otherwise return False 
	''' 
	def add_patient_by_info(self, patient_email, other_pat_info):
		if not any(patient.email == patient_email for patient in self._patients):
			patient = Patient(patient_email, other_pat_info)
			self._providers.append(provider)
			return patient	# Success, return new patient object
		else:
			return False	# Failed (already in patients)
	'''
	def add_patient(self, patient):
		if patient not in self._patients:	
			self._patients.append(patient)
			return 		# Success
		else:
			return False	# Failed (already in patients)


	def add_provider(self, provider):
		if provider not in self._providers:	
			self._providers.append(provider)
			return True		# Success
		else:
			return False	# Failed (already in patients)

	def remove_patient(self, patient_email):
		# if any(patient.email == patient_email for patient in self._patients):
		#	remove
		#	return true
		# OR
		# for i, patient in self._patients:
		# 	if patient.email == patient_email:
		# 		del self._patients[i]
		# 		return True
		# return False
		pass

	def remove_provider(self, provider_email):
		# if any(provider.email == provider_email for provider in providers):
		#	remove
		#	return true
		# OR
		# for i, provider in self._providers:
		# 	if provider.email == provider_email:
		# 		del self._providers[i]
		# 		return True
		# return False
		pass

	
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
		pass


