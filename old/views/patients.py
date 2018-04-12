from flask import render_template, request
from sqlalchemy import or_

from app import app
from app.models.diseases import Disease
from app.models.patients import Patient
from app.views.users import User


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
        data={'patient': patient, 'user': user }
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
