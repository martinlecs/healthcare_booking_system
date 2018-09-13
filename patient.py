from user import User

class Patient(User):
	"Patient class"
	def __init__(self, email, password, surname, given_name, medicare_no, appointments = []):
		super().__init__(email, password, surname, given_name, appointments)
		self._medicare_no = medicare_no

	@property
	def medicare_no(self):
		return self._medicare_no

	@medicare_no.setter
	def medicare_no(self, medicare_no):
		self._medicare_no = medicare_no

# from user import User

# class Patient(User):
# 	"Patient class"
# 	def __init__(self, email, password, surname, givenName, medicareNo, appointments=[]):
# 		super().__init__(email, password)
# 		self._surname = surname
# 		self._givenName = givenName
# 		self._medicareNo = medicareNo
# 		self._appointments = appointments

# 	@property
# 	def surname(self):
# 		return self._surname

# 	@property
# 	def givenName(self):
# 		return self._givenName

# 	@property
# 	def medicareNo(self):
# 		return self._medicareNo

# 	@property
# 	def appointments(self):
# 		return self._appointments

# 	@medicareNo.setter
# 	def medicareNo(self, medicareNo):
# 		self._medicareNo = medicareNo

# 	@appointments.setter
# 	def appointments(self, appointments):
# 		self._appointments = appointments
