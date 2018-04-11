import hashlib

from passlib.apps import custom_app_context as pwd_context

from app.models import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.Unicode)
    first_name = db.Column(db.Unicode)
    last_name = db.Column(db.Unicode)
    # hire_date = db.Column(db.Date)
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def register(self):
        pass
        # TODO: Register a new nurse

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def update_password(self, new_password):
        self.password = pwd_context.encrypt(new_password)

    def generate_token(self):
        h = hashlib.sha1()
        h.update(
            '{0}{1}{2}'.format(self.id, self.email, self.password).encode()
        )
        return h.hexdigest()

    def verify_token(self, token):
        return token == self.generate_token()

    def password_reset(self, reset_link):
        pass

    def __repr__(self):
        return "<User(id='{}', first_name='{}', last_name='{}', email='{}', password={},is_admin='{}')>".format(self.id, self.first_name, self.last_name, self.email,
                                                                   self.password, self.is_admin)



