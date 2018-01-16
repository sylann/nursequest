import os

from flask import Flask

from app.models import db


basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, '..', 'nursequest.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
