from routes import app, centre_manager, user_manager

# Run app
if __name__ == '__main__':
    app.run(debug=True)

    print('Testing Persistence')
    print(centre_manager.centres)
    for prov in user_manager.providers:
        print(prov.email, "rating: ", prov.average_rating)
    
    #Save everything
    print('Saving')
    centre_manager.save_data()
    user_manager.save_data()
    print('Save complete')
    