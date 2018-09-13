from user import User

class Provider(User):
	"Provider class"
	def __init__(self, email, password, surname, given_name,
	provider_no, service, appointments = [], centres=[], availability=[], rating=[]):
		super().__init__(email, password, surname, given_name, appointments)
		self._provider_no = provider_no
		self._service = service
		self._centres = centres
		self._availability = availability
		self._rating = []

	@property
	def provider_no(self):
		return self._provider_no

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
	def rating(self):
		return self._rating

	@provider_no.setter
	def provider_no(self, provider_no):
		self._provider_no = provider_no

	@service.setter
	def service(self, service):
		self._service = service

	@centres.setter
	def centres(self, centres):
		self._centres = centres

	@availability.setter
	def availability(self, availability):
		self._availability = availability

	@rating.setter
	def rating(self, rating):
		self._rating = rating
