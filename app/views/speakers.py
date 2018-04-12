from pprint import pprint

from flask import render_template, request, redirect, url_for, session
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.speakers import Speaker
from app.models.needs import Need

@app.route('/need_page/<int:id>')
def get_need_page(id):
    need = Need.query.filter_by(id=id).first()

    return render_template('speakers/need-page-speaker.html',
                           data={'need': need},
                           title='Page de demande',
                           subtitle=session['name'])

@app.route('/need_validation/<int:id>')
def get_need_validation(id):
    need = Need.query.filter_by(id=id).first()

    return render_template('speakers/need-validation.html',
                           data={'need': need},
                           title='Page de validation d\'une demande',
                           subtitle=session['name'])

@app.route('/validate_need', methods=['POST'])
def need_validate(id):

    token = request.form.get('token')
    appraisal = request.form.get('appraisal')

    need = Need.query.filter_by(id=id).first()

    return render_template('speakers/need-validation.html',
                           data={'need': need},
                           title='Page de validation d\'une demande',
                           subtitle=session['name'])

@app.route('/speaker/dashboard/<int:id>')
def get_speaker_dashboard(id):
    print('cc je passe par speaker')
    speaker = Speaker.query.get(id)
    print(speaker)

    needs = Need.query.filter_by(id_assigned_speaker=speaker.id).all()
    print(needs)
    return render_template('speakers/speaker-dashboard.html',
                           data={'speaker': speaker,
                                 'attribute_needs': needs},
                           title='Dashboard',
                           subtitle=session['name'])

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
