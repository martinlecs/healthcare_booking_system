from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from server import app, user_manager, centre_manager, appt_manager, notifications_manager, permissions
from model.provider import Provider
from model.system import correct_identity
from model.date_validity import date_valid
from model.error import *
from datetime import date, datetime, time

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.context_processor
def inject_services_into_all_templates():
	return dict(services=[''] + user_manager.get_service_names()) #Details for the drop down box

@app.context_processor
def inject_current_user_into_all_templates():
	return dict(curr_user=current_user)

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
		if provider is False:
			if request.form['medicare_no']:
				user.medicare_no = request.form['medicare_no']
		content = user.get_information()
		user_manager.save_data()

	if provider:
		centre_name_to_id = {}
		for centre in content['centres']:
			centre_obj = centre_manager.get_centre_from_name(centre)
			centre_name_to_id[centre] = centre_obj.id
		return render_template('user_profile.html', content=content, provider=provider, centres=centre_name_to_id)

	return render_template('user_profile.html', content=content, provider=provider)


@login_required
@app.route('/book/<provider>_<centre>', methods=['GET','POST'])
def book(provider, centre):
	"""
	Renders Booking Page
	:param provider: a provider email
	:param centre: a centre id
	:return: booking.html if all works out, otherwise 'Something Wrong?'
	"""
	# Check that provider and centre exist
	try:
		p = user_manager.get_user(provider)
	except IdentityError as e:
		raise e
	try:
		c = centre_manager.get_centre_from_id(centre)
	except IdentityError as e:
		raise e


	# Check that provider is associated with centre
	if c.name.lower() not in p.centres:
		raise BookingError("Provider isn't associated with centre")

	# If current user is the chosen provider, render error template
	if p.email.lower() == current_user.email.lower():
		raise BookingError("Provider can't book an appointment with themselves")
	# If a specialist, check for a referral
	if p.specialist is True:
		user = user_manager.get_user(current_user.email)
		if provider not in user.referrals:
			raise BookingError("You need a referral to book with this specialist")
	
	today = date.today().isoformat()

	reason = request.args.get("reason")
	if reason is None or reason is "":
		reason = " "
	form_date = request.args.get("date")
	if form_date is not "" and form_date is not None:
		try:
			date_valid(form_date)
		except DateTimeValidityError as e:
			raise e
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
	
	# Check that provider and centre exist
	try:
		p = user_manager.get_user(provider)
	except IdentityError as e:
		raise e
	try:
		c = centre_manager.get_centre_from_id(centre)
	except IdentityError as e:
		raise e
	
	# Check that provider is associated with centre
	if c.name.lower() not in p.centres:
		raise BookingError("Provider isn't associated with centre")
	
	# make appointment object
	# 
	try:
		appt = appt_manager.make_appt_and_add_appointment_to_manager(current_user.email, provider, centre, date, time_slot, reason)
	except BookingError as e:
		raise e
	except DateTimeValidityError as e:
		raise e

	if appt not in appt_manager.appointments:
		raise BookingError("Booking isn't being saved")
	# Add appts object to patient and provider
	current_user.add_appointment(appt)
	if appt not in current_user.appointments:
		raise BookingError("Booking isn't being saved in current user")
	
	p.add_appointment(appt)
	if appt not in p.appointments:
		raise BookingError("Booking isn't being saved in provider")

	if p.specialist is True:
		user = user_manager.get_user(current_user.email)
		try:
			user.rem_referral(p.email)
		except:
			pass #Do not want system to crash on exception, system can go on without this

	# Make time slot unavailable
	date_split = date.split('-')
	year = int(date_split[0])
	month = int(date_split[1])
	day = int(date_split[2])
	try:
		p.make_time_slot_unavailable(c.name, year, month, day, time_slot)
	except BookingError as e:
		appt_manager.remove_appointment(appt.id)
		raise e
	except DateTimeValidityError as e:
		appt_manager.remove_appointment(appt.id)
		raise e
	
	user_manager.save_data()
	appt_manager.save_data()

	# send notification to patient
	notifications_manager.add_notification(provider, current_user.get_id())
	
	return render_template('booking_confirmed.html', prov_name=user_manager.get_user(appt.provider_email).fullname, centre_name=centre_manager.get_centre_from_name(c.name).name, date=appt.date, time=appt.time_slot)
	

@login_required
@app.route('/provider/<provider>', methods=['GET','POST'])
def provider_profile(provider):
	"""
	Renders a provider profile
	:param user: a Provider email
	:return: renders the provider_profile.html template
	"""
	try:
		p = user_manager.get_user(provider)
	except IdentityError as e:
		raise e

	if request.method == 'POST':
		rating = int(request.form['rate'])
		p.add_rating(current_user.get_id(), rating)
		user_manager.save_data()
	content = p.get_information()
	centre_name_to_id = {}
	for centre in content['centres']:
		try:
			centre_obj = centre_manager.get_centre_from_name(centre)
			centre_name_to_id[centre] = centre_obj.id
		except IdentityError:
			pass # Still want to present profile page if centre returns error
	return render_template('provider_profile.html', content=content, centres=centre_name_to_id)

@login_required
@app.route('/centre/<centre>', methods=['GET','POST'])
def centre_profile(centre):
	"""
	Creates a centre profile page
	:param centre: a Centre id
	:return: renders the centre_profile.html template
	"""
	try:
		c = centre_manager.get_centre_from_id(centre)
	except IdentityError as e:
		raise e

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
	try:
		p = user_manager.get_user(patient)
	except IdentityError as e:
		raise e
	
	content = p.get_information()
	appointments = p.get_upcoming_appointments() + p.get_past_appointments()

	return render_template('patient_profile.html', content=content, appointments=appointments)

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
	correct_identity(current_user, current_user)

	user = user_manager.get_user(current_user.get_id())
	if type(user) is Provider:
		prov_view = True
	else:
		prov_view = False
	user.set_past_appointments()
	arg = 'current'
	if request.args.get('appt'):
		arg = request.args.get('appt')

	content = {}
	if arg == "current":
		appt = user.get_upcoming_appointments()
	elif arg == "past":
		appt = user.get_past_appointments()
	elif arg == "ref":
		appt = user.referrals.values()
	else:
		raise AppointmentError("Appointment History not Found")

	# content['current'] = [x.get_information() for x in cur_appt]
	# content['past'] = [x.get_information() for x in past_appt]
	# # This isn't particularly pretty now, will refactor eventually
	content = [x.get_information() for x in appt]
	if arg != "ref":
		for appt in content:
			prov = user_manager.get_user(appt['provider_email'])
			appt['prov_name'] = " ".join([prov.given_name, prov.surname])
			patient = user_manager.get_user(appt['patient_email'])
			appt['patient_name'] = " ".join([patient.given_name, patient.surname])
			appt['centre_name'] = centre_manager.get_centre_from_id(appt['centre_id']).name
	# for appt in content['past']:
	# 	prov = user_manager.get_user(appt['provider_email'])
	# 	appt['prov_name'] = " ".join([prov.given_name, prov.surname])
	# 	patient = user_manager.get_user(appt['patient_email'])
	# 	appt['patient_name'] = " ".join([patient.given_name, patient.surname])
	# 	appt['centre_name'] = centre_manager.get_centre_from_id(appt['centre_id']).name
	return render_template('appointment_history.html', content=content, prov_view=prov_view, arg=arg)


@login_required
@app.route('/appointment/<apptid>', methods=['GET','POST'])
def view_appointment(apptid):

	try:
		appt = appt_manager.search_by_id(int(apptid))
	except IdentityError as e:
		raise e

	edit = False
	gp = False
	user = user_manager.get_user(current_user.get_id())
	if type(user) is Provider:
		identity = user_manager.get_user(appt.provider_email)
		if appt.past is False:
			edit = True
		if user.service == "gp":
			gp = True
	else:
		identity = user_manager.get_user(appt.patient_email)

	if permissions.check_permissions(current_user.get_id(), appt.patient_email):
		pass
	elif user.email == appt.patient_email:
		pass
	elif not correct_identity(identity, user):
		raise IdentityError("Wrong user for Appointment")

	if request.method == 'POST':
		if request.form['notes']:
			appt.notes = {'provider': current_user.get_id(), 'notes': request.form['notes']}
		if request.form['meds']:
			appt.add_meds(request.form["meds"])
		user_manager.save_data()
		appt_manager.save_data()

	content = appt.get_information()
	prov = user_manager.get_user(appt.provider_email)
	content['prov_name'] = " ".join([prov.given_name, prov.surname])
	patient = user_manager.get_user(content['patient_email'])
	content['patient_name'] = " ".join([patient.given_name, patient.surname])
	content['centre_name'] = centre_manager.get_centre_from_id(content['centre_id']).name
	content['meds'] = ", ".join(content['meds'])
	return render_template('appointment.html',content=content, edit=edit, gp=gp)

@login_required
@app.route('/appointment/<apptid>/referral', methods=['GET','POST'])
def referral(apptid):
	
	appt = appt_manager.search_by_id(int(apptid))
	user = user_manager.get_user(current_user.get_id())
	
	if type(user) is Provider:
    		identity = user_manager.get_user(appt.provider_email)
	else:
    		identity = user_manager.get_user(appt.patient_email)
	correct_identity(identity, user)
	
	specialist = user_manager.specialists()
	if request.method == 'POST':
		patient = user_manager.get_user(appt.patient_email)
		spec = request.form['ref_tgt']
		gp = appt.provider_email
		msg = request.form['ref_msg']
		patient.add_referral(spec,gp,msg)
		print(patient.referrals)
		print(spec)
		user_manager.save_data()
		content = {"spec": spec, "patient": patient.email, "msg":msg}
		return render_template('referral.html', apptid=apptid, specialist=specialist, content=content)
    
	return render_template('referral.html', apptid=apptid, specialist=specialist)


@login_required
@app.route('/notifications', methods=['GET', 'POST'])
def notifications():
	print(permissions.display_all_permissions())

	if request.method == 'POST':
		notifications_manager.get_notification(current_user.get_id(), request.form['submit_button']).process_notification()
		permissions.save_data()
		notifications_manager.remove_notification(current_user.get_id() ,request.form['submit_button'])
		# notifications_manager.save_data()
		return render_template('notifications.html', notifications=notifications_manager.get_all_notifications(current_user.get_id()))

	return render_template('notifications.html', notifications=notifications_manager.get_all_notifications(current_user.get_id()))


@login_manager.user_loader
def load_user(email):
	return user_manager.get_user(email)

@app.errorhandler(IdentityError)
def handle_identity_error(error):
	return render_template('error_identity.html', msg=error.msg)

@app.errorhandler(BookingError)
def handle_booking_error(error):
	return render_template('error.html', error_msg=error.msg)

@app.errorhandler(DateTimeValidityError)
def handle_date_time_validity_error(error):
	return render_template('error.html', error_msg=error.msg)
	
@app.errorhandler(404)
def handle_404_error(error):
	return render_template('error_404.html'), 404

@app.errorhandler(ValueError)
def handle_value_error(error):
	return render_template('error.html', error_msg=error.msg)
	
