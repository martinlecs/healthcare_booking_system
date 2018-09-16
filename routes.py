from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from system import SystemManager
from server import app, user_manager, centre_manager, appt_manager
from date_validity import is_date_valid

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
	logout_user()
	return redirect(url_for('index'))


@login_required
@app.route('/book/<provider>_<centre>', methods=['GET','POST'])
def book(provider, centre):
	p = user_manager.get_user(provider)
	c = centre_manager.get_centre_from_id(centre)
	# if request.method == 'POST':
	# 	date = request.form["date"]
	# 	# validity = is_date_valid(year, month, day)
	# 	# if validity is True:
	# 	return redirect(url_for('index'))

	reason = request.args.get("reason")
	if reason is None:
		reason = ""
	date = request.args.get("date")
	if date is not "" and date is not None:
		date_split = date.split('-')
		year = int(date_split[0])
		month = int(date_split[1])
		day = int(date_split[2])
		# get availability
		avail = p.get_availability(c.name, year, month, day)
		if avail != None:
			return render_template('booking.html', date=date, reason=reason, provider=p, centre=c, available_slots=avail, date_chosen=True)
		else:
			return 'fuck'
	else:
		return render_template('booking.html', provider=p, centre=c, date_chosen=False, error=True)



@login_required
@app.route('/book_confirmation/<provider>_<centre>_<date>_<time_slot>_<reason>', methods=['GET','POST'])
def book_confirmation(provider, centre, date, time_slot, reason):
	p = user_manager.get_user(provider)
	c = centre_manager.get_centre_from_id(centre)
	# make appointment object
	appt = appt_manager.make_appt_and_add_appointment_to_manager(current_user.email, provider, centre, date, time_slot, reason)
	if appt == False:
		return 'crap'
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
		return 'shit biscuit'
	return redirect(url_for('index'))
	

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


""" 
Depending on what radio button is selected, uses the respective
user or centre search function which returns a list of appropriate 
objects to iterate through and display
"""
@login_required
@app.route('/search', methods=['POST'])
def search():
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



@login_manager.user_loader
def load_user(email):
	return user_manager.get_user(email)
