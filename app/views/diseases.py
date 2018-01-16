from flask import request, render_template, redirect, url_for
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models.diseases import Disease
from app.utils import get_all_diseases


@app.route('/diseases')
def get_diseases():
    q = Disease.query
    searched = request.args.get('search')
    if searched is not None:
        q = q.filter(Disease.name.ilike('%' + searched + '%'))
    diseases = q.all()
    return render_template('diseases.html', diseases=diseases)


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
    except IntegrityError as err:
        print(err.args[0])
        db.session.rollback()
    return redirect(url_for('get_diseases'))