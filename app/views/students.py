from flask import render_template, request, redirect, url_for, session, abort

from sqlalchemy import or_

from app import app, db
from app.models.students import Student
from app.models.needs import Need
from app.models.speakers import Speaker



@app.route('/student/need/<int:id>')
def get_need_page_student(id):
    """
    Renvoie le résumé d'un need
    :return:
    """
    student = Student.query.filter_by(id_user=session['uid']).first()
    try:
        need = Need.query.get(id)
    except:
        abort(500)
    return render_template('students/need-page-student.html',
                           data={'need': need,
                                 'student': student},
                           title='Résumé du besoin')

@app.route('/student/need/<int:id>/close', methods=['POST'])
def close_need(id):
    """
    Quand on clique sur 'terminer' un besoin validé par un intervenant
    :param id: id du besoin
    :return: dashboard étudiant
    """

    try:
        need = Need.query.get(id)
    except:
        abort(500)

    need.status = 'Terminé'
    if need.team.tokens < 0:
        need.team.tokens = 0
    else:
        need.team.tokens -= need.used_tokens

    try:
        db.session.commit()
    except:
        abort(500)

    return redirect(url_for('get_student_dashboard'))


@app.route('/student/need/new/select-speaker')
def get_select_speaker():
    """
    Renvoie la page de sélection d'un intervenant
    :return:
    """
    speakers = Speaker.query.filter_by(role=False).all()
    student = Student.query.filter_by(id_user=session['uid']).first()


    return render_template(
        'students/speaker-choice.html',
        current_route='get_select_speaker',
        title='Choisir son intervenant',
        data=speakers,
        student=student)


@app.route('/students/need/new/<int:id>')
def get_create_need(id):
    """
    Renvoie la page de création d'un besoin
    :return:
    """
    speaker = Speaker.query.get(id)
    student = Student.query.filter_by(id_user=session['uid']).first()

    return render_template('students/create-need.html',
                           title='Définir votre besoin',
                           data={'speaker': speaker,
                                 'student': student}
                           )


@app.route('/students/need/new', methods=['POST'])
def create_need():
    """
    Créé le besoin en db
    :return:
    """
    student = Student.query.filter_by(id_user=session['uid']).first()

    title = request.form.get('title')
    description = request.form.get('description')
    speaker_id = request.form.get('speaker_id')
    estimated_tokens = int(request.form.get('estimated_tokens'))

    if estimated_tokens < 0:
        estimated_tokens = 0

    need = Need(
        title=title,
        description=description,
        estimated_tokens=estimated_tokens,
        status='En cours',
        id_assigned_team=student.team.id,
        id_assigned_speaker=speaker_id
    )

    db.session.add(need)
    try:
        db.session.commit()
    except:
        abort(500)

    return redirect(url_for('get_student_dashboard'))


@app.route('/student/dashboard')
def get_student_dashboard():
    """
    Pagine et renvoie le dashboard utilisateur
    :return:
    """
    student = Student.query.filter_by(id_user=session['uid']).first()
    q = Need.query.filter_by(id_assigned_team=student.team.id)
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Need.title.ilike('%' + searched + '%'),
            Need.description.ilike('%' + searched + '%'),
            Need.status.ilike('%' + searched + '%'),
        ))
    needs = q.paginate(page, 5, False)

    return render_template(
        'students/project-stage.html',
        current_route='get_student_dashboard',
        title=student.team.project.title,
        subtitle='Retrouvez ici l\'ensemble de vos demandes !',
        data=needs,
        student=student,
        searched=searched
    )
