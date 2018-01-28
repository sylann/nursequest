from flask import request, render_template, redirect, url_for
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models.diseases import Disease
from app.utils import get_all_diseases


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


@app.route('/diseases/update')
def refresh_diseases():
    for d in get_all_diseases():
        existing = Disease.query.filter_by(link=d.get('href')).first()
        if existing:
            continue
        new_disease = Disease(name=d.text, link=d.get('href'))
        db.session.add(new_disease)
    try:
        db.session.commit()
        return redirect(url_for('get_diseases'))
    except IntegrityError as err:
        app.logger.error(err.args[0])
        db.session.rollback()
        return jsonify({ 'error': err })
