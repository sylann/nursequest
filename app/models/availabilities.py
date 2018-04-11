from app.models import db
from app.models.speakers import Speaker


class Availabilities(db.Model):
    __tablename__ = 'availabilities'

    id = db.Column(db.Integer, primary_key=True)
    date_begin = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)

    id_assigned_speaker = db.Column(db.Integer, db.ForeignKey(Speaker.id, name="fk_assigned_speaker_id"))
    speaker = db.relationship('Speaker', lazy='joined')

    def __repr__(self):
        return "<Availabilities (id='{}, date_begin='{}', date_end='{}', id_speaker='{}')>".format(
            self.id, self.date_begin, self.date_end, self.id_assigned_speaker)
