from pprint import pprint

from flask import render_template, request, redirect, url_for, session, abort
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.ideas import Ideas
from app.models.users import User


@app.route('/ideas')
def get_ideas():
    q = Ideas.query
    print(q)
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Ideas.title.ilike('%' + searched + '%'),
            Ideas.description.ilike('%' + searched + '%')
        ))
    ideas = q.paginate(page, 10, False)
    return render_template(
        'ideas.html',
        current_route='get_ideas',
        title='Liste des idées proposées',
        subtitle='',
        data=ideas,
        searched=searched
    )


@app.route('/ideas/new/')
def get_create_idea():
    user = User.query.filter_by(id=session['uid']).first()

    return render_template(
        'create_idea.html',
        title='Proposez une nouvelle idée de projet',
        data={'user': user}
        )


@app.route('/ideas/create_idea', methods=['POST'])
def create_idea():
    user = User.query.filter_by(id=session['uid']).first()
    title = request.form.get('title')
    description = request.form.get('description')

    print(session)
    print(user)

    idea = Ideas(
        title=title,
        description=description,
        id_user=user.id,
        interested=1
    )

    db.session.add(idea)
    try:
        db.session.commit()
    except:
        abort(500)

    return redirect(url_for('get_ideas'))


@app.route('/ideas/add_interest_idea/<int:id>')
def add_interest_idea(id):

    idea = Ideas.query.filter_by(id=id).first()
    idea.interested = idea.interested + 1

    try:
        db.session.commit()
    except:
        abort(500)

    return redirect(url_for('get_ideas'))
