from flask import render_template, request, redirect, url_for, session, abort
from sqlalchemy import or_

from app import app, db
from app.models.students import Student
from app.models.projects import Project
from app.models.teams import Team


@app.route('/teams')
def get_teams():
    """
        Pagine et renvoie toutes les teams
        :return:
        """
    q = Team.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Team.name.ilike('%' + searched + '%'),
            Team.description.ilike('%' + searched + '%')
        ))
    teams = q.paginate(page, 5, False)
    return render_template(
        'teams.html',
        current_route='get_teams',
        title='Liste des équipes',
        subtitle='',
        data=teams,
        searched=searched
    )


@app.route('/team/new')
def get_create_team():
    """
    Renvoie la page de création d'équipe
    :return:
    """
    students = Student.query.filter(Student.id_assigned_team == None, Student.id_user != session['uid']).all()
    projects = Project.query.all()

    return render_template(
        'teams/team-creation.html',
        title='Créer une équipe',
        data={'students': students,
              'projects': projects}
    )


@app.route('/team/created', methods=['POST'])
def create_team():
    """
    Crée une équipe en DB
    :return:
    """
    raise NotImplementedError
    # name = request.form.get('name')
    # description = request.form.get('description')
    # tokens = request.form.get('tokens')
    #
    # team = Team(
    #     name=name,
    #     description=description
    # )
    #
    # db.session.add(team)
    # try:
    #     db.session.commit()
    # except:
    #     abort(500)
    #
    # return redirect(url_for('get_ideas'))
    # students = request.form.get('users')
    # project = request.form.get('project')
    #
    # return redirect(url_for('get_teams'))
