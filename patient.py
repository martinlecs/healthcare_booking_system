from user import User
# Anything marked with *** means my own implemenation

class Patient(User):
	# "Patient class"
	# def __init__(self, email, password, surname, givenName, medicareNo, appointments):
	def __init__(self, email, password, surname, givenName):
	# 	user = User(self, email, password)
		super().__init__(email, password)
		self._surname = surname
		self._givenName = givenName
		self._medicareNo = ""	#***
		self._appointments = []	#

	@property
	def surname(self):
		return self._surname

	@property
	def givenName(self):
		return self._givenName

	@property
	def medicareNo(self):
		return self._medicareNo

	@property
	def appointments(self):
		return self._appointments

	@medicareNo.setter
	def medicareNo(self, medicareNo):
	    self._medicareNo = medicareNo

	@appointments.setter
	def appointments(self, appointments):
		self._appointments = appointments