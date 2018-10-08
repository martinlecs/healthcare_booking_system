from datetime import date, datetime, time

def date_valid(given_date):
	date_split = given_date.split('-')
	year = int(date_split[0])
	month = int(date_split[1])
	day = int(date_split[2])
	new_date = date(year, month, day)
	if new_date < date.today():
		return False
	else:
		return True

def time_slot_to_time(time_slot):
		time_slot = time_slot.split(':')
		hour_ = int(time_slot[0])
		minute_ = int(time_slot[1])
		return time(hour = hour_, minute = minute_)


def time_valid(time_slot):
	now_time = time_slot_to_time(datetime.now().time().isoformat(timespec='minutes'))
	
	time_slot = time_slot.split(':')
	hour_ = int(time_slot[0])
	minute_ = int(time_slot[1])
	time_slot_in_time = time(hour = hour_, minute = minute_)

	if now_time > time_slot_in_time:
		return False