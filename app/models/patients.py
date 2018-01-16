from app.models import db
from app.models.users import User


class CaughtDisease(db.Model):
    __tablename__ = 'caught_diseases'

    id_patient = db.Column(db.ForeignKey('patients.id', name='pk_fk_patient'), primary_key=True)
    id_disease = db.Column(db.ForeignKey('diseases.id', name='pk_fk_disease'), primary_key=True)
    contracted = db.Column(db.DateTime)
    disease = db.relationship('Disease')


class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Unicode)
    last_name = db.Column(db.Unicode)
    address = db.Column(db.Unicode)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    job = db.Column(db.String)
    social_number = db.Column(db.String, unique=True)
    latest_admission = db.Column(db.DateTime)
    latest_medical_exam = db.Column(db.DateTime)
    diseases = db.relationship('CaughtDisease')
    id_assigned_user = db.Column(db.Integer, db.ForeignKey(User.id, name="fk_assigned_user_id"))
    assigned_user = db.relationship('User', lazy='joined', backref=db.backref('patients', lazy=True))

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def assign(self, user):
        if self.id_assigned_user is None:
            self.id_assigned_user = user.id
            print("Inform {} he is now taking care of {}".format(
                user.full_name, self.full_name)
            )
            return True
        return False

    def unassign(self):
        print("Inform {} he is no longer taking care of {}".format(
            self.assigned_user.full_name, self.full_name)
        )
        self.id_assigned_user = None
