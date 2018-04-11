from os.path import join as path_join

from flask import render_template, send_file

from app import app
from app.views import *


@app.route('/')
def index():
    print("TTTTTTTTTTTTTTTTTTTTZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    return render_template(
        'home.html',
        title='Bienvenue sur WETA !',
        subtitle='Workshop Enhanced Token Administration'
    )


@app.route('/')
def ideas():
    return render_template(
        'ideas.html',
        title='Liste des idées proposées'
    )


@app.route('/')
def projects():
    return render_template(
        'projects.html',
        title='Bienvenue sur WETA !',
        subtitle='Workshop Enhanced Token Administration'
    )


@app.route('/')
def teams():
    return render_template(
        'teams.html',
        title='Bienvenue sur WETA !',
        subtitle='Workshop Enhanced Token Administration'
    )


@app.route('/static/<path:path>')
def get_static(path):
    try:
        return send_file(path_join(app.root_path, "static", path))
    except IOError as e:
        pass
    return "Not Found", 404
