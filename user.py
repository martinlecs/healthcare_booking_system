from flask_login import UserMixin

class User(UserMixin):
	"User class"
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

	def get_id(self):
		return self._email
