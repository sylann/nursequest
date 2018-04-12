from flask import render_template, request, redirect, url_for, session
from sqlalchemy import or_

from app import app
from app.views.students import get_student_dashboard
from app.models.users import User
from app.models.speakers import Speaker
from app.models.availabilities import Availabilities
from app.models.needs import Need
from app.models.students import Student
from app.models.ideas import Ideas


@app.route('/login')
def get_login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.clear()
    return render_template('login.html', error='Vous avez bien été déconnecté')

@app.route('/login', methods=['POST'])
def login():

    login = request.form.get('login').lower()
    password = request.form.get('password')
    try:
        #On check s'il existe un utilisateur avec ce login en tant qu'email
        user = User.query.filter_by(email=login).first()
        print(user)

        #On check si le mot de passe de cet utilisateur correspond bien
        if user.verify_password(password):

            #On regarde si cet utilisateur est un speaker, si oui on le récupère
            check_speaker = Speaker.query.filter_by(id_assigned_user=user.id).first()
            session['uid'] = user.id
            session['name'] = user.first_name

            #Si on récupère bien un objet speaker, on vérifie si c'est un intervenant (role null)
            if check_speaker and not check_speaker.role:
                session['logged_as'] = 'speaker'
                return redirect(url_for('get_speaker_dashboard', id=check_speaker.id))

            #Si on récupère bien un objet speaker, on vérifie si c'est un responsable pédago (role true)
            elif check_speaker and check_speaker.role:
                session['logged_as'] = 'main_teacher'
                return redirect(url_for('get_mainteacher_dashboard', id=check_speaker.id))

            #Si on ne récupère pas d'objet speaker
            else:

                #On regarde si cet utilisateur est un student, si oui on le récupère
                check_student = Student.query.filter_by(id_user=user.id).first()

                #Si on récupère bien un objet student
                if check_student:
                    session['logged_as'] = 'student'
                    print(session)
                    return redirect(url_for('get_student_dashboard'))

                #Sinon, l'utilisateur existe bien mais il est ni un speaker, ni un student
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