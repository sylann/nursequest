from app.models import db
from app.models.users import User
from app.models.teams import Team


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String)

    id_user = db.Column(db.Integer, db.ForeignKey(User.id, name="fk_assigned_user_id"))
    user = db.relationship('User', lazy='joined')

    id_assigned_team = db.Column(db.Integer, db.ForeignKey(Team.id, name="fk_assigned_team_id"))
    team = db.relationship('Team', lazy='joined')

    def __repr__(self):
        return "<Student (id='{}, degree='{}', id_user='{}', id_assigned_team='{}')>".format(
                self.id, self.degree, self.id_user, self.id_assigned_team)
