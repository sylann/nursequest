from app.models import db
from app.models.projects import Project


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    logo = db.Column(db.String)
    tokens = db.Column(db.Integer)
    description = db.Column(db.String)

    id_assigned_project = db.Column(db.Integer, db.ForeignKey(Project.id, name="fk_assigned_project_id"))
    assigned_project = db.relationship('Project', lazy='joined')

    def __repr__(self):
        return "<Team (id='{}, name='{}', logo='{}', tokens='{}', description='{}', id_assigned_project='{}')>".format(
            self.id, self.name, self.logo, self.tokens, self.description, self.id_assigned_project)
