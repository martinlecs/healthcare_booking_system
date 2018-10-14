class IdentityError(Exception):
    def __init__(self, msg):
        super().__init__(self)
        self.msg = msg

class BookingError(Exception):
	def __init__(self, msg):
		super().__init__(self)
		self.msg = msg

class AppointmentError(Exception):
	def __init__(self, msg):
		super().__init__(self)
		self.msg = msg

class DateTimeValidityError(Exception):
	def __init__(self, msg):
		super().__init__(self)
		self.msg = msg	