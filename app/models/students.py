from app.models import db
from app.views.users import User
from app.models.teams import Team


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String)
    logo = db.Column(db.String)
    tokens = db.Column(db.Integer)
    description = db.Column(db.String)

    id_user = db.Column(db.Integer, db.ForeignKey(User.id, name="fk_assigned_user_id"))
    user = db.relationship('User', lazy='joined')

    id_assigned_team = db.Column(db.Integer, db.ForeignKey(Team.id, name="fk_assigned_team_id"))
    assigned_team = db.relationship('Team', lazy='joined')

    ideas = db.relationship('Ideas')

    def __repr__(self):
        return "<Student (id='{}, degree='{}', logo='{}', tokens='{}', description='{}', id_user='{}', " \
               "id_assigned_team='{}')>".format(
                self.id, self.degree, self.logo, self.tokens, self.description, self.id_user, self.id_assigned_team)
