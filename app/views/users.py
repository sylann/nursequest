from flask import render_template, request, redirect, url_for
from sqlalchemy import or_

from app import app
from app.views.students import get_student_dashboard
from app.models.users import User
from app.models.ideas import Ideas


@app.route('/login')
def login():
    return redirect(url_for('get_student_dashboard', id=2))



@app.route('/forgotten-password')
def forgottenpwd():
    return render_template('forgotten-password.html')


@app.route('/ideas')
def get_ideas():
    q = Ideas.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Ideas.id.ilike('%' + searched + '%'),
            Ideas.title.ilike('%' + searched + '%'),
            Ideas.description.ilike('%' + searched + '%'),
            Ideas.id_student.ilike('%' + searched + '%')
        ))
    ideas = q.paginate(page, 15, False)
    print(ideas)
    return render_template(
        'ideas.html',
        current_route='get_ideas',
        title='Liste des idées proposées',
        subtitle='',
        data=ideas,
        searched=searched
    )


@app.route('/projects')
def get_projects():
    return render_template('projects.html')


@app.route('/teams')
def get_teams():
    return render_template('teams.html')


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
