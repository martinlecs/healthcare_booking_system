class IdentityError(Exception):
    def __init__(self, msg):
        super().__init__(self)
        self.msg = msg

class BookingError(Exception):
	def __init__(self, msg):
		super().__init__(self)
		self.msg = msg