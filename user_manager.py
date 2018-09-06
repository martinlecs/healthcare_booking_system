# from patient import Patient
# from provider import Provider


class UserManager:
	"User manager skeleton"
	def __init__(self):
		self._patients = []
		self._providers = []

	@property
	def patients(self):
		return self._patients
	
	@property
	def providers(self):
		return self._providers
	
	def add_patient(self, patient):
		if patient not in self._patients:	
			self._patients.append(patient)
			return True		# Success
		else:
			return False	# Failed (already in patients)

	def add_provider(self, provider):
		if provider not in self._providers:	
			self._providers.append(provider)
			return True		# Success
		else:
			return False	# Failed (already in patients)

	def remove_patient(self, patient_email):
		# patient in patients
		# if any(patient.email == patient_email for patient in patients):
		# 	remove
		#	return True
		# else
		#	return False
		pass