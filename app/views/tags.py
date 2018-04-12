from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.tags import UserTag

# @app.route('/tags')
# def get_tags():
#     q = UserTag.query
#     page = request.args.get('page', default=1, type=int)
#     searched = request.args.get('search', default='')
#     if searched:
#         q = q.filter(or_(
#             User.first_name.ilike('%' + searched + '%'),
#             User.last_name.ilike('%' + searched + '%'),
#             User.email.ilike('%' + searched + '%')
#         ))
#     users = q.paginate(page, 10, False)
#     return render_template(
#         'users.html',
#         current_route='get_users',
#         title='List of hired nurses',
#         subtitle='',
#         data=users,
#         searched=searched
#     )
