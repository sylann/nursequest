from pprint import pprint

from flask import render_template, request, redirect, url_for, session
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.students import Student
from app.models.projects import Project


@app.route('/teams')
def get_teams():
    return render_template(
        'teams.html',
        current_route='get_teams',
        title='Liste des équipes'
    )


@app.route('/team/new')
def get_create_team():
    students = Student.query.filter(Student.id_assigned_team == None, Student.id_user != session['uid']).all()
    projects = Project.query.all()

    return render_template(
        'teams/team-creation.html',
        title='Créer une équipe',
        data={'students': students,
              'projects': projects}
    )


@app.route('/team/created', methods=['POST'])
def create_team():
    students = request.form.get('users')
    project = request.form.get('project')

    print(type(students), project)
    return redirect(url_for('get_login'))
