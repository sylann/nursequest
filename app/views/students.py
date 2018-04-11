from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import cast
import datetime

from app import app, db
from app.models.students import Student
from app.models.needs import Need


@app.route('/student/dashboard/<int:id>')
def get_student_dashboard(id):
    student = Student.query.get(id)
    print(student.team.project)
    print(student.team)

    needs = Need.query.filter_by(id_assigned_team=student.team.id).all()
    print('TTTTTTTTTTTTTTt', needs)

    #Team : Name, tokens restants
    #Projet : titre / desc
    #Needs : intervenant / nb tokens

    return render_template('students/project-stage.html',
                           data={'student': student,
                                 'team_needs': needs},
                           title='Dashboard')

@app.route('/student')
def get_student():
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