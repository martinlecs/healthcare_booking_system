from datetime import date

# Module to return date validity #
'''
Returns:
	True == valid!
	False == non-int function arguments
	None == year, month or day values out of range, OR date in past 
'''
def is_date_valid(year, month, day):
		if type(year) is not int or type(month) is not int or type(day) is not int:
			return False	# Invalid type
		if year < 2018 or (month < 1 or month > 12) or (day < 1 or day > 31):
			return None		# invalid date values
		if date(year, month, day) < date.today():
			return None		# day in the past
		return True