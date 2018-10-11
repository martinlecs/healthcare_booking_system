from model.user import User

class Patient(User):
	"Patient class"
	def __init__(self, email, password, surname, given_name, medicare_no): #appointments=[]
		super().__init__(email, password, surname, given_name)
		self._medicare_no = medicare_no

	@property
	def medicare_no(self):
		return self._medicare_no

	@medicare_no.setter
	def medicare_no(self, medicare_no):
		self._medicare_no = medicare_no

	def get_information(self):
		return { 'email': self.email,
				 'surname': self.surname,
				 'given_name': self.given_name,
				 'fullname': self.fullname,
				 'medicare_no': self._medicare_no,
				}
