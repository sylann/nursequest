from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.speakers import Speaker


@app.route('/mainteacher/dashboard/<int:id>')
def get_mainteacher_dashboard(id):
    mainteacher = Speaker.query.get(id)

    return render_template(
        'mainteachers/main-teacher-dashboard.html',
        data={'mainteacher': mainteacher},
        title='Bienvenue ' + mainteacher.user.full_name,
        subtitle='Responsable Pédagogique')

