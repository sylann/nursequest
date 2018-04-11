from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.patients import Patient

@app.route('/ideas')
def get_ideas():
    q = Patient.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Patient.first_name.ilike('%' + searched + '%'),
            Patient.last_name.ilike('%' + searched + '%'),
            Patient.email.ilike('%' + searched + '%'),
            Patient.social_number.ilike('%' + searched + '%')
        ))
    patients = q.paginate(page, 10, False)
    return render_template(
        'patients.html',
        current_route='get_patients',
        title='List of admitted patients',
        subtitle='',
        data=patients,
        searched=searched
    )