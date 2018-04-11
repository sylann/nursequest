from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.teams import Team


@app.route('/teams')
def get_teams():
    return render_template(
        'teams.html',
        current_route='get_teams',
        title='Liste des équipes'
    )
