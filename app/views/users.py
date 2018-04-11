from flask import render_template, request, redirect, url_for, session
from sqlalchemy import or_

from app import app
from app.views.students import get_student_dashboard
from app.models.users import User
from app.models.speakers import Speaker
from app.models.availabilities import Availabilities
from app.models.needs import Need
from app.models.students import Student


@app.route('/login')
def get_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    try:
        user = User.query.filter_by(email=login).first()
        print(user)
        if user.verify_password(password):
            check_speaker = Speaker.query.filter_by(UserID=user.UserID).first()
            if check_speaker and check_speaker.Role == 0:
                session['logged_as'] = 'speaker'
                return render_template('speakers/speaker-dashboard.html')
            elif check_speaker and check_speaker.Role == 1:
                session['logged_as'] = 'main_teacher'
                return render_template('mainteachers/main-teacher-dashboard.html')
            else:
                check_student = Student.query.filter_by(UserID=user.UserID).first()
                if check_student:
                    session['logged_as'] = 'student'
                    return render_template('students/project-stage.html')
                else:
                    render_template('login.html', error='Votre compte est en cours de validation')

        else:
            return render_template('login.html', error='Mauvais mot de passe')
    except Exception as e:
        print(e)
        return render_template('login.html', error='Cet identifiant n\'existe pas')

@app.route('/forgotten-password')
def forgottenpwd():
    return render_template('forgotten-password.html')


@app.route('/users')
def get_users():
    q = User.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            User.first_name.ilike('%' + searched + '%'),
            User.last_name.ilike('%' + searched + '%'),
            User.email.ilike('%' + searched + '%')
        ))
    users = q.paginate(page, 10, False)
    return render_template(
        'users.html',
        current_route='get_users',
        title='List of hired nurses',
        subtitle='',
        data=users,
        searched=searched
    )


@app.route('/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    return render_template(
        'user.html',
        current_route='get_user',
        title=user.full_name,
        data=user
    )