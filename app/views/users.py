from flask import render_template, request
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models.users import User
from app.utils import generate_fake_user


@app.route('/login')
def login():
    return render_template('login.html')


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
    return user.full_name


@app.route('/users/fake/<int:quantity>')
def fake_users(quantity):
    i = 0
    while i < quantity:
        new_user = User(**generate_fake_user())
        db.session.add(new_user)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()
            return "Server Error", 500
    return "OK", 200