from abc import ABC 

class User(ABC):
	"Abstract user class"
	def __init__(self, email, password):
		self._email = email
		self._password = password

	@property
	def email(self):
		return self._email
	
	@property
	def password(self):
		return self._password
	
	@email.setter
	def email(self, email):
		self._email = email

	@password.setter
	def password(self, pwd):
		self._password = pwd



