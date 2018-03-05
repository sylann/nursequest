from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.diseases import Disease
from app.models.patients import Patient, CaughtDisease
from app.models.users import User
from app.utils import generate_fake_patient, generate_random_list, generate_patient_date, fake


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
    try:
        user = User.query.get(patient.id_assigned_user)
    except:
        pass
        # TODO : To be finished

    return render_template(
        'patient.html',
        current_route='get_patient',
        title=patient.full_name,
        data={'patient': patient, 'user': user}
    )

@app.route('/patients/new')
def get_add_patient():
    users = User.query.all()
    # TODO : Mieux filtrer users (id - full_name)
    diseases = Disease.query.all()

    return render_template(
        'add_patient.html',
        current_route='get_add_patient',
        title='Add patient',
        data={'users': users, 'diseases': diseases}
    )

@app.route('/patients/new', methods=['POST'])
def add_patient():
    pprint(request.args)
    nurse_id = request.form.get('nurse')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    address = request.form.get('address')
    email = request.form.get('email')
    phone = request.form.get('phone')
    job = request.form.get('job')
    social_number = request.form.get('social_number')
    disease_id = str(request.form.get('disease'))
    latest_admission = datetime.datetime.now()
    contracted = datetime.datetime.strptime(request.form.get('contracted'), '%Y-%m-%d')

    if nurse_id == '0':
        nurse_id = None

    patient = Patient(
        first_name=first_name,
        last_name=last_name,
        address=address,
        email=email,
        phone=phone,
        job=job,
        social_number=social_number,
        latest_admission=latest_admission,
        latest_medical_exam=fake.date_time_between_dates(
            datetime_start=datetime.datetime.now(),
            datetime_end=datetime.datetime.now()),
        id_assigned_user=nurse_id
    )

    db.session.add(patient)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return "Server Error", 500

    db.session.refresh(patient)
    caught_disease = CaughtDisease(
        id_patient=patient.id,
        id_disease=disease_id,
        contracted=contracted
    )

    db.session.add(caught_disease)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return "Server Error", 500

    return redirect(url_for('get_patients'))

@app.route('/patient/edit/<int:id>')
def get_edit_patient(id):
    patient = Patient.query.get(id)
    # Todo : Mieux filtrer la requete (id/fullname)
    users = User.query.all()

    return render_template(
        'edit_patient.html',
        current_route='get_update_patient',
        title='Edit ' + patient.full_name,
        data={'users': users, 'patient': patient}
    )

@app.route('/patient/edit/<int:id>', methods=['POST'])
def edit_patient(id):
    # Todo : Vérifier que l'id existe ?
    print('*********************************************')
    print(id)
    patient = Patient.query.get(id)

    nurse_id = request.form.get('nurse')
    patient.first_name = request.form.get('first_name')
    patient.last_name = request.form.get('last_name')
    patient.address = request.form.get('address')
    patient.email = request.form.get('email')
    patient.phone = request.form.get('phone')
    patient.job = request.form.get('job')

    if nurse_id == '0':
        patient.id_assigned_user = None
    else:
        patient.id_assigned_user = nurse_id

    db.session.flush()
    db.session.commit()

    return redirect(url_for('get_patients'))

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
