from patient import Patient
from flask import render_template, request, redirect, url_for

@app.route("/patient_list_appointments", methods=['GET'])
def patient_list_appointments(appointments):
    return render_template("patient_list_appointments.html", appointments=appointments)

@app.route("/provider_list_appointments", methods=['GET'])
def provider_list_appointments(appointments):
    return render_template"provider_list_appointments.html", appointments=appointments)
