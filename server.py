from flask import Flask
from user_manager import UserManager

# Instantiate 'global' variables

app = Flask(__name__)
app.secret_key = 'super secret shhhh'

user_manager = UserManager()
user_manager.add_patient_by_info('jack@gmail.com', 'cs1531','Burman', 'Jack', '067562343')
user_manager.add_patient_by_info('tom@gm', 'cs1531','Lake', 'Tom', '546742535')
user_manager.add_patient_by_info('isaac@gmail.com', 'cs1531','Smith', 'Isaac', '512441235')
user_manager.add_patient_by_info('hao@gmail.com', 'cs1531','Wong', 'Hao', '12324535')

user_manager.add_provider_by_info('toby@gmail.com','cs1531', 'Jackson', 'Toby', '34646184', 'Pathologist')
user_manager.add_provider_by_info('sid@gmail.com','cs1531', 'Troy', 'Sid', '462312184', 'Pathologist')
user_manager.add_provider_by_info('gary@gmail.com','cs1531', 'Pluman', 'Gary', '462312184', 'GP')
user_manager.add_provider_by_info('samuel@gmail.com','cs1531', 'Marks', 'Samuel', '945612184', 'GP')
user_manager.add_provider_by_info('anna@gmail.com','cs1531', 'Stanalovski', 'Anna', '894563553', 'GP')
user_manager.add_provider_by_info('michael@gmail.com','cs1531', 'Pearson', 'Michael', '263478656', 'Physiotherapist')
user_manager.add_provider_by_info('ian@gmail.com','cs1531', 'Thorp', 'Ian', '36997657', 'Physiotherapist')
user_manager.add_provider_by_info('thomas@gmail.com','cs1531', 'Tank', 'Thomas', '372341657', 'Pharmacist')
# centre_manager = CentreManager()