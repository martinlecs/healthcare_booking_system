from user import User
# Anything marked with *** means my own implemenation

class Provider(User):
	"Provider class"
	# def __init__(self, email, password, surname, givenName, providerNo, service,
 	#   			centres, availability, appointments, rating):
	def __init__(self, email, password, surname, givenName):	#***
		super().__init__(email, password)	#***
		self._surname = surname
		self._givenName = givenName
		self._providerNo = ""	#***
		self._service = ""	#***
		self._centres = []	#***
		self._availability = []	#***
		self._appointments = []	#***
		self._rating = 0	#***

	@property
	def surname(self):
		return self._surname

	@property
	def givenName(self):
		return self._givenName

	@property
	def providerNo(self):
		return self._providerNo

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
	def appointments(self):
		return self._appointments

	@property
	def rating(self):
		return self._rating

	@providerNo.setter
	def providerNo(self, providerNo):
	    self._providerNo = providerNo

	@centres.setter
	def centres(self, centres):
		self._centres = centres

	@availability.setter
	def availability(self, availability):
		self._availability = availability

	@appointments.setter
	def appointments(self, appointments):
		self._appointments = appointments

	@rating.setter
	def rating(self, rating):
		self._rating = rating
