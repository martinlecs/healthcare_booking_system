from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from server import app, user_manager, centre_manager, appt_manager
from model.provider import Provider
from model.system import correct_identity
from model.date_validity import date_valid, date_and_time_valid, date_string_to_date
from model.error import *
from datetime import date, datetime, time

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.context_processor
def inject_services_into_all_templates():
	return dict(services=[''] + user_manager.get_service_names()) #Details for the drop down box

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	"""
	Logs In User
	:return: Redirects on access approved
	"""
	if request.method == 'POST':
		email = request.form["email"].strip().lower()
		password = request.form["password"].lower()
		user = user_manager.is_valid_user(email, password)
		if user is not None:
			login_user(user)
			return redirect(url_for('index'))
		else:
			return render_template('login.html', invalid_login=True)
	return render_template('login.html', invalid_login=False)

@app.route('/logout')
@login_required
def logout():
	"""
	Logs out current user
	:return: redirect to index, which redirects to login
	"""
	logout_user()
	return redirect(url_for('index'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def user_profile():
	"""
	Renders Current User's Profile
	:return: user_profile.html if all works out
	"""
	user = load_user(current_user.get_id())
	provider = False
	content = user.get_information()
	if type(user) is Provider:
    		provider = True
	if request.args.get('edit'):
		return render_template('user_profile.html', content=content, edit=True, provider=provider)

	if request.method == 'POST':
		if request.form['given_name']:
			user.given_name = request.form['given_name']
		if request.form['surname']:
			user.surname = request.form['surname']
		if request.form['medicare_no']:
			user.medicare_no = request.form['medicare_no']
		content = user.get_information()
		user_manager.save_data()

	centre_name_to_id = {}
	for centre in content['centres']:
		centre_obj = centre_manager.get_centre_from_name(centre)
		centre_name_to_id[centre] = centre_obj.id
	
	return render_template('user_profile.html', content=content, provider=provider, centres=centre_name_to_id)


@login_required
@app.route('/book/<provider>_<centre>', methods=['GET','POST'])
def book(provider, centre):
	"""
	Renders Booking Page
	:param provider: a provider email
	:param centre: a centre id
	:return: booking.html if all works out, otherwise 'Something Wrong?'
	"""
	# date_split = 
	p = user_manager.get_user(provider)
	c = centre_manager.get_centre_from_id(centre)
	
	# If current user is the chosen provider, render error template
	if p.email.lower() == current_user.email.lower():
		raise BookingError("Provider can't book an appointment with themselves")

	today = date.today().isoformat()

	reason = request.args.get("reason")
	if reason is None or reason is "":
		reason = " "
	form_date = request.args.get("date")
	if form_date is not "" and form_date is not None and date_valid(form_date) != False:
		date_split = form_date.split('-')
		year = int(date_split[0])
		month = int(date_split[1])
		day = int(date_split[2])
		avail = p.get_availability(c.name, year, month, day)
		if avail != None:
			return render_template('booking.html', today=today, date=form_date, reason=reason, provider=p, centre=c, available_slots=avail, date_chosen=True)
		else:
			raise BookingError("Time slot not available")
	else:
		return render_template('booking.html', today=today, provider=p, centre=c, date_chosen=False, error=True)



@login_required
@app.route('/book_confirmation/<provider>_<centre>_<date>_<reason>_<time_slot>', methods=['GET','POST'])
def book_confirmation(provider, centre, date, time_slot, reason):
	"""
	Submmits Booking request
	:param provider: a provider email
	:param centre: a centre id
	:param date: a date in form of string
	:param time_slot: string
	:param reason: string
	:return: redirects to index function if all works out, otherwise 'Something Wrong?'
	"""
	# if date_and_time_valid(time_slot, date) == False:
	# 	raise BookingError("Invalid date or time")

	p = user_manager.get_user(provider)
	c = centre_manager.get_centre_from_id(centre)
	# make appointment object
	# 
	try:
		appt = appt_manager.make_appt_and_add_appointment_to_manager(current_user.email, provider, centre, date, time_slot, reason)
	except BookingError as e:
		raise e
	# appt = appt_manager.make_appt_and_add_appointment_to_manager(current_user.email, provider, centre, date, time_slot, reason)
	# if appt == False:
	# 	raise BookingError("Booking taken OR provider and patient same person")
	
	# 	# return render_template('error.html', error_msg="Booking taken OR provider and patient same person")	# redirect to home page and display an error message
	# Add appts object to patient and provider
	current_user.add_appointment(appt)
	p.add_appointment(appt)
	# Make time slot unavailable
	date_split = date.split('-')
	year = int(date_split[0])
	month = int(date_split[1])
	day = int(date_split[2])
	checker = p.make_time_slot_unavailable(c.name, year, month, day, time_slot)
	if checker != True:
	# if checker == False:
		return 'Something Wrong?'
	user_manager.save_data()
	appt_manager.save_data()
	return render_template('booking_confirmed.html', prov_name=p.fullname, centre_name=c.name, date=date, time=time_slot)
	

@login_required
@app.route('/provider/<provider>', methods=['GET','POST'])
def provider_profile(provider):
	"""
	Renders a provider profile
	:param user: a Provider email
	:return: renders the provider_profile.html template
	"""
	p = user_manager.get_user(provider)
	if request.method == 'POST':
		rating = int(request.form['rate'])
		p.add_rating(current_user.get_id(), rating)
		user_manager.save_data() 
	content = p.get_information()
	centre_name_to_id = {}
	for centre in content['centres']:
		centre_obj = centre_manager.get_centre_from_name(centre)
		centre_name_to_id[centre] = centre_obj.id
	return render_template('provider_profile.html', content=content, centres=centre_name_to_id)

@login_required
@app.route('/centre/<centre>', methods=['GET','POST'])
def centre_profile(centre):
	"""
	Creates a centre profile page
	:param centre: a Centre id
	:return: renders the centre_profile.html template
	"""
	c = centre_manager.get_centre_from_id(centre)
	if request.method == 'POST':
		rating = int(request.form['rate'])
		c.add_rating(current_user.get_id(), rating)
		centre_manager.save_data() 
	content = c.get_information()
	return render_template('centre_profile.html', content=content)


@login_required
@app.route('/patient/<patient>', methods=['GET'])
def patient_profile(patient):
	"""
	Creates a centre profile page
	:param centre: a Centre id
	:return: renders the centre_profile.html template
	"""
	p = user_manager.get_user(patient)
	content = p.get_information()
	return render_template('patient_profile.html', content=content)

@login_required
@app.route('/search', methods=['POST'])
def search():
	""" 
	Returns search results of providers/centres depending on
	search category
	:param query: search term and category
	:return: renders search_results.html with table of results
	"""
	if request.form['type']:
		query = request.form['search']
		select = request.form.get('type', 'centre_name') #for now
		results = []

		if select == 'c_name':
			results = centre_manager.search_name(query)
			type_c = True
		elif select == 'c_suburb':
			results = centre_manager.search_suburb(query)
			type_c = True
		elif select == 'p_name':
			results = user_manager.search_name(query)
			type_c = False
		else:
			results = user_manager.search_service(select)
			type_c = False

		if not results:
			error = "No matches found"
		else:
			# error = "Please select a search category"
			error = None

		return render_template('search_results.html', results=results, type_c=type_c, error=error)
	else:
		return redirect(url_for('index'))

@app.route('/not_a_secret', methods=['GET'])
def not_a_secret():
	return render_template('not_a_secret.html')

@login_required
@app.route('/appointments', methods=['GET'])
def appointment_history():
	if not correct_identity(current_user, current_user):
		raise IdentityError("Wrong user for URL")
	
	user = user_manager.get_user(current_user.get_id())
	if type(user) is Provider:
		prov_view = True
	else:
		prov_view = False
	
	cur_appt = user.get_upcoming_appointments()
	past_appt = user.get_past_appointments()
	
	content = {}
	content['current'] = [x.get_information() for x in cur_appt]
	content['past'] = [x.get_information() for x in past_appt]
	# This isn't particularly pretty now, will refactor eventually
	for appt in content['current']:
		prov = user_manager.get_user(appt['provider_email'])
		appt['prov_name'] = " ".join([prov.given_name, prov.surname])
		patient = user_manager.get_user(appt['patient_email'])
		appt['patient_name'] = " ".join([patient.given_name, patient.surname])
		appt['centre_name'] = centre_manager.get_centre_from_id(appt['centre_id']).name
	for appt in content['past']:
		prov = user_manager.get_user(appt['provider_email'])
		appt['prov_name'] = " ".join([prov.given_name, prov.surname])
		patient = user_manager.get_user(appt['patient_email'])
		appt['patient_name'] = " ".join([patient.given_name, patient.surname])
		appt['centre_name'] = centre_manager.get_centre_from_id(appt['centre_id']).name
	 
	return render_template('appointment_history.html', content=content, prov_view=prov_view)


@login_required
@app.route('/appointments/<apptid>', methods=['GET','POST'])
def view_appointment(apptid):
	appt = appt_manager.search_by_id(int(apptid))
	edit = False
	# if appt is False:
	# 	raise IdentityError("404")
	# Validate identity for appointment first
	user = user_manager.get_user(current_user.get_id())
	if type(user) is Provider:
		identity = user_manager.get_user(appt.provider_email)
		if appt.past is False:
			edit = True
	else:
		identity = user_manager.get_user(appt.patient_email)

	if not correct_identity(identity, user):
		raise IdentityError("Wrong user for Appointment")
	content = appt.get_information()


	return render_template('appointment.html',content=content, edit=edit)


@login_manager.user_loader
def load_user(email):
	return user_manager.get_user(email)

@app.errorhandler(IdentityError)
def handle_identity_error(error):
	return render_template('error_identity.html')

@app.errorhandler(BookingError)
def handle_booking_error(error):
	return render_template('error.html', error_msg=error.msg)
	
@app.errorhandler(404)
def handle_404_error(error):
	return render_template('error_404.html'), 404
	
