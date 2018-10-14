class Referral():
    def __init__(self, specialist, gp, msg):
        self._specialist = specialist
        self._gp = gp
        self._msg = msg

    @property
    def specialist(self):
        return self._specialist
    
    @property
    def gp(self):
        return self._gp
    
    @property
    def msg(self):
        return self._msg

    def get_information(self):
        return {"spec":self._specialist,
                "gp": self._gp,
                "msg": self._msg
                }

