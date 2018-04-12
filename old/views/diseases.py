import datetime

from flask import request, render_template, redirect, url_for
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models.diseases import Disease
from app.models.models_old.diseases import Disease
from old.utils import get_all_diseases


@app.route('/diseases')
def get_diseases():
    q = Disease.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(Disease.name.ilike('%' + searched + '%'))
    diseases = q.paginate(page, 10, False)
    return render_template(
        'diseases.html',
        current_route='get_diseases',
        title='List of all known diseases',
        subtitle='These are really bad bad things',
        data=diseases,
        searched=searched
    )