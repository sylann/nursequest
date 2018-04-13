from app.models import db
from app.models.users import User


class Ideas(db.Model):
    __tablename__ = 'ideas'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    interested = db.Column(db.Integer)

    id_user = db.Column(db.Integer, db.ForeignKey(User.id, name="fk_user_id"))
    user = db.relationship('User', lazy='joined')

    def __repr__(self):
        return "<Ideas (id='{}, title='{}', description='{}', id_user='{}', interested='{}')>".format(
            self.id, self.title, self.description, self.id_user, self.interested)





