
from flask import render_template, request
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models.diseases import Disease
from app.models.patients import Patient, CaughtDisease
from app.utils import generate_fake_patient, generate_random_list, generate_patient_date


@app.route('/patients')
def get_patients():
    q = Patient.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Patient.first_name.ilike('%' + searched + '%'),
            Patient.last_name.ilike('%' + searched + '%'),
            Patient.email.ilike('%' + searched + '%'),
            Patient.social_number.ilike('%' + searched + '%')
        ))
    patients = q.paginate(page, 10, False)
    return render_template(
        'patients.html',
        current_route='get_patients',
        title='List of admitted patients',
        subtitle='',
        data=patients,
        searched=searched
    )


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


