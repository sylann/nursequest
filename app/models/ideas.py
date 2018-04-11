from app.models import db
from app.models.students import Student


class Ideas(db.Model):
    __tablename__ = 'ideas'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    id_student = db.Column(db.Integer, db.ForeignKey(Student.id, name="fk_student_id"))
    student = db.relationship('Student', lazy='joined')

    def __repr__(self):
        return "<Ideas (id='{}, title='{}', description='{}', id_student='{}')>".format(
            self.id, self.title, self.description, self.id_student)





