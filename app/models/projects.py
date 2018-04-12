from app.models import db


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    min_members = db.Column(db.Integer)
    max_members = db.Column(db.Integer)
    token_number = db.Column(db.Integer)
    description = db.Column(db.String)

    def __repr__(self):
        return "<Project (id='{}, min_members='{}', max_members='{}', token_number='{}', description='{}')>".format(
            self.id, self.min_members, self.max_members, self.token_number, self.description)
