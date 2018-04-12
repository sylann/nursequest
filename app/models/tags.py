from app.models import db
from app.views.users import User


class IdeaTag(db.Model):
    __tablename__ = 'idea_tag'

    id_tag = db.Column(db.ForeignKey('tags.id', name='pk_fk_ideatag_tag'), primary_key=True)
    id_idea = db.Column(db.ForeignKey('ideas.id', name='pk_fk_ideatag_idea'), primary_key=True)

    def __repr__(self):
        return "<IdeaTag (id_tag='{}, id_idea='{}')>".format(self.id_tag, self.id_idea)


class UserTag(db.Model):
    __tablename__ = 'user_tag'

    id_tag = db.Column(db.ForeignKey('tags.id', name='pk_fk_usertag_tag'), primary_key=True)
    id_user = db.Column(db.ForeignKey('users.id', name='pk_fk_usertag_user'), primary_key=True)

    def __repr__(self):
        return "<UserTag (id_tag='{}, id_user='{}')>".format(self.id_tag, self.id_user)


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    type = db.Column(db.Unicode)

    id_assigned_user = db.Column(db.Integer, db.ForeignKey(User.id, name="fk_assigned_user_id"))
    user = db.relationship('User', lazy='joined')

    def __repr__(self):
        return "<Project (id='{}, name='{}', type='{}', id_assigned_user='{}')>".format(
            self.id, self.name, self.type, self.id_assigned_user)




