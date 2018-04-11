from app.models import db
from app.models.users import User
from app.models.needs import Need


class Speaker(db.Model):
    __tablename__ = 'speakers'

    id = db.Column(db.Integer, primary_key=True)
    tokens = db.Column(db.Integer)
    role = db.Column(db.Boolean)

    id_assigned_user = db.Column(db.Integer, db.ForeignKey(User.id, name="fk_assigned_user_id"))
    user = db.relationship('User', lazy='joined')

    def __repr__(self):
        return "<Speaker (id='{}, tokens='{}', role='{}', id_assigned_user='{}')>".format(
            self.id, self.tokens, self.role, self.id_assigned_user)
