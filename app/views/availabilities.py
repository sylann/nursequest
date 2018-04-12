from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import or_

from app import app
from app.models.availabilities import Availabilities


@app.route('/availabilities')
def get_availabilities():
    """
    Pagine et renvoie toutes les availabilities
    :return:
    """
    q = Availabilities.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Availabilities.id.ilike('%' + searched + '%'),
            Availabilities.date_begin.ilike('%' + searched + '%'),
            Availabilities.date_end.ilike('%' + searched + '%'),
            Availabilities.id_assigned_speaker.ilike('%' + searched + '%')
        ))
    availabilities = q.paginate(page, 15, False)
    return render_template(
        'availabilities.html',
        current_route='get_availabilities',
        title='Liste des disponibilités de cet intervenant',
        data=availabilities,
        searched=searched
    )
