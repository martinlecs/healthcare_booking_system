from routes import app #, centre_manager, user_manager, appt_manager

# Run app
if __name__ == '__main__':

	app.run(debug=True)

	#Save everything
	# print('Saving')
	# centre_manager.save_data()
	# user_manager.save_data()
	# appt_manager.save_data()
	# print('Save complete')
