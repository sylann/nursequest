from flask import Flask

from app.models import db
from app.models.users import User
from app.models.patients import Patient
from app.models.diseases import Disease


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
