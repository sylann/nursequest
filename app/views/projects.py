from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.projects import Project

@app.route('/projects')
def get_projects():
    q = Project.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Project.first_name.ilike('%' + searched + '%'),
            Project.last_name.ilike('%' + searched + '%'),
            Project.email.ilike('%' + searched + '%'),
            Project.social_number.ilike('%' + searched + '%')
        ))
    projects = q.paginate(page, 10, False)
    return render_template(
        'projects.html',
        current_route='get_projects',
        title='List of admitted patients',
        subtitle='',
        data=projects,
        searched=searched
    )