from datetime import date, datetime, time
from model.error import DateTimeValidityError

def date_valid(given_date):
	"""
	If given_date < today => Invalid!
	"""
	try:
		new_date = date_string_to_date(given_date)
	except DateTimeValidityError as e:
		raise e
		# raise DateTimeValidityError("Invalid date")
	
	if new_date < date.today():
		return False
	else:
		return True

def time_slot_to_time(time_slot):
	try:
		time_slot = time_slot.split(':')
		hour_ = int(time_slot[0])
		minute_ = int(time_slot[1])
		new_time = time(hour = hour_, minute = minute_)
	except:
		raise DateTimeValidityError("Invalid time")

	return new_time

def date_string_to_date(given_date):
	try:
		date_split = given_date.split('-')
		year = int(date_split[0])
		month = int(date_split[1])
		day = int(date_split[2])
		new_date = date(year, month, day)
	except:
		raise DateTimeValidityError("Invalid date")

	return new_date

def date_and_time_valid(time_slot, given_date):
	"""
	If given time and date is in the past => Invalid
	"""
	s = " ".join([given_date, time_slot])
	try:
		d = datetime.strptime(s,"%Y-%m-%d %H:%M")
	except:
		raise DateTimeValidityError("Invalid date and/or time")
	
	if d < datetime.now():
		raise DateTimeValidityError("Date or time in the past")

	# if not date_valid(given_date):
	# 	return False

	# given_date = date_string_to_date(given_date)

	# now_time = time_slot_to_time(datetime.now().time().isoformat(timespec='minutes'))
	
	# time_slot = time_slot_to_time(time_slot)

	# if given_date == date.today():
	# 	if now_time > time_slot:
	# 		return False
	# else:
	# 	return True