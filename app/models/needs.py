from app.models import db
from app.models.teams import Team
from app.models.speakers import Speaker


class Need(db.Model):
    __tablename__ = 'needs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    estimated_tokens = db.Column(db.Integer)
    status = db.Column(db.String)
    speaker_conclusion = db.Column(db.String)
    team_conclusion = db.Column(db.String)
    used_tokens = db.Column(db.Integer)
    # creation_date = db.Column(db.DateTime)
    # validation_date = db.Column(db.DateTime)
    # close_date = db.Column(db.DateTime)

    id_assigned_team = db.Column(db.Integer, db.ForeignKey(Team.id, name="fk_assigned_team_id"))
    team = db.relationship('Team', lazy='joined')

    id_assigned_speaker = db.Column(db.Integer, db.ForeignKey(Speaker.id, name="fk_assigned_speaker_id"))
    speaker = db.relationship('Speaker', lazy='joined')

    def __repr__(self):
        return "<Need (id='{}, title='{}', description='{}', estimated_tokens='{}', status='{}, " \
               "speaker_conclusion='{}', team_conclusion='{}', close_date='{}', id_team='{}', id_speaker='{}')>".format(
                self.id, self.title, self.description, self.estimated_tokens, self.status, self.speaker_conclusion,
                self.team_conclusion, self.used_tokens, self.id_assigned_team, self.id_assigned_speaker)
