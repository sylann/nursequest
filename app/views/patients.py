
from flask import render_template
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models.diseases import Disease
from app.models.patients import Patient, CaughtDisease
from app.utils import generate_fake_patient, generate_random_list, generate_patient_date


@app.route('/patients')
def get_patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)


@app.route('/patients/<int:id>')
def get_patient(id):
    patient = Patient.query.get(id)
    return patient.full_name


@app.route('/patients/fake/<int:quantity>')
def fake_patients(quantity):
    i = 0
    while i < quantity:
        new_patient = Patient(**generate_fake_patient())
        db.session.add(new_patient)
    try:
        db.session.commit()
        i += 1
    except IntegrityError:
        db.session.rollback()
        return "Server error", 500
    return "OK", 200


@app.route('/patients/fake/caught_diseases')
def fake_caught_diseases():
    for id_patient in generate_random_list(Patient):
        for id_disease in generate_random_list(Disease):
            new_catch = CaughtDisease(
               id_patient=id_patient,
               id_disease=id_disease,
               contracted=generate_patient_date()
            )
            db.session.add(new_catch)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()


