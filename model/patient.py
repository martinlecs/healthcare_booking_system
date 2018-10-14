from model.user import User
from model.referral import Referral

class Patient(User):
	"Patient class"
	def __init__(self, email, password, surname, given_name, medicare_no): #appointments=[]
		super().__init__(email, password, surname, given_name)
		self._medicare_no = medicare_no
		self._referrals = {}

	@property
	def medicare_no(self):
		return self._medicare_no
	
	@property
	def referrals(self):
		return self._referrals

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

	def add_referral(self, specialist, gp, msg):
		ref = Referral(specialist, gp, msg)
		self._referrals[specialist] = ref

	def rem_referral(self, key):
		res = self._referrals.pop(key)
