from os.path import join as path_join

from flask import send_file

from app.views.users import *
from app.views.patients import *
from app.views.diseases import *


@app.route('/')
def index():
    return render_template(
        'home.html',
        title='Welcome to Nurse Quest!',
        subtitle='Take care of your patients'
    )


@app.route('/static/<path:path>')
def get_static(path):
    try:
        return send_file(path_join(app.root_path, "static", path))
    except IOError as e:
        pass
    return "Not Found", 404
