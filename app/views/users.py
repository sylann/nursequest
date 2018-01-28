from flask import render_template, request
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models.users import User
from app.utils import generate_fake_user


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/users')
def get_users():
    page = request.args.get('page', default=1, type=int)
    users = User.query.paginate(page, 10, False)
    return render_template(
        'users.html',
        current_route='get_users',
        title='List of hired nurses',
        subtitle='',
        data=users
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