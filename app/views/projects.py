from pprint import pprint

from flask import render_template, request, redirect, url_for, session, abort
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.projects import Project
from app.models.ideas import Ideas
from app.models.users import User


@app.route('/projets')
def get_projects():
    """
    Pagine et renvoie la liste des projets
    :return:
    """
    q = Project.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Project.title.ilike('%' + searched + '%'),
            Project.description.ilike('%' + searched + '%')
        ))
    projects = q.paginate(page, 10, False)
    return render_template(
        'projects.html',
        current_route='get_projects',
        title='Liste des projets en cours',
        subtitle='',
        data=projects,
        searched=searched
    )


@app.route('/projects/new/')
def get_create_project():
    user = User.query.filter_by(id=session['uid']).first()

    return render_template(
        'create_project.html',
        title='Création d\'un nouveau projet de Workshop',
        data={'user': user}
        )


@app.route('/projects/create_project', methods=['POST'])
def create_project():
    user = User.query.filter_by(id=session['uid']).first()
    title = request.form.get('title')
    description = request.form.get('description')
    min_members = request.form.get('min_members')
    max_members = request.form.get('max_members')
    token_number = request.form.get('token_number')

    project = Project(
        title=title,
        description=description,
        min_members=min_members,
        max_members=max_members,
        token_number=token_number
    )

    db.session.add(project)
    try:
        db.session.commit()
    except:
        abort(500)

    return redirect(url_for('get_projects'))


# @app.route('/ideas/add_interest_idea/<int:id>')
# def add_interest_idea(id):
#
#     idea = Ideas.query.filter_by(id=id).first()
#     idea.interested = idea.interested + 1
#
#     try:
#         db.session.commit()
#     except:
#         abort(500)
#
#     return redirect(url_for('get_ideas'))
