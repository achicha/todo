from flask_bcrypt import generate_password_hash, check_password_hash
from ..database import db  # pragma: no cover


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    #posts = relationship("Post", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password).decode('utf-8')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):  # pragma: no cover
        return '<name - {}>'.format(self.name)
