from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.ideas import Ideas


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
    print(ideas)
    return render_template(
        'ideas.html',
        current_route='get_ideas',
        title='Liste des idées proposées',
        subtitle='',
        data=ideas,
        searched=searched
    )


@app.route('/new_idea')
def new_idea():
    return render_template(
        'new_idea.html',
        current_route='new_idea',
        title='Proposez une nouvelle idée de projet',
        subtitle=''
    )
