from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.speakers import Speaker

@app.route('/speaker/dashboard/<int:id>')
def get_speaker_dashboard(id):
    print('cc je passe par speaker')
    speaker = Speaker.query.get(id)
    print(speaker)

    return render_template('speakers/speaker-dashboard.html',
                           data={'speaker': speaker})

@app.route('/speakers')
def get_speakers():
    q = Speaker.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Speaker.id.ilike('%' + searched + '%'),
            Speaker.role.ilike('%' + searched + '%'),
            Speaker.tokens.ilike('%' + searched + '%')
        ))
    speakers = q.paginate(page, 10, False)
    return render_template(
        'speakers.html',
        current_route='get_speakers',
        title='Liste des intervenants disponibles',
        subtitle='',
        data=speakers,
        searched=searched
    )
