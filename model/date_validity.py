from datetime import date, datetime, time

def date_valid(given_date):
	"""
	If given_date < today => Invalid!
	"""
	new_date = date_string_to_date(given_date)
	if new_date < date.today():
		return False
	else:
		return True

def time_slot_to_time(time_slot):
		time_slot = time_slot.split(':')
		hour_ = int(time_slot[0])
		minute_ = int(time_slot[1])
		return time(hour = hour_, minute = minute_)

def date_string_to_date(given_date):
	date_split = given_date.split('-')
	year = int(date_split[0])
	month = int(date_split[1])
	day = int(date_split[2])
	return date(year, month, day)

def date_and_time_valid(time_slot, given_date):
	"""
	If given_date < today => Invalid!
	If given_day is today but time_slot is before current time => Invalid!
	Else => VALID!
	"""
	if not date_valid(given_date):
		return False

	given_date = date_string_to_date(given_date)

	now_time = time_slot_to_time(datetime.now().time().isoformat(timespec='minutes'))
	
	time_slot = time_slot_to_time(time_slot)

	if given_date == date.today():
		if now_time > time_slot:
			return False
	else:
		return True
