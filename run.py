from routes import app, centre_manager

# Run app
if __name__ == '__main__':
    app.run(debug=True)

    #Save everything
    print('Saving')
    centre_manager.save_data()
    print('Save complete')
    