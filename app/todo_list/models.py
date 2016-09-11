from sqlalchemy import ForeignKey  # pragma: no cover
from sqlalchemy.orm import relationship, backref  # pragma: no cover

from app.database import db
import datetime
from ..login.models import User

"""SQLAlchemy models"""


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))
    # Use cascade='delete,all' to propagate the deletion of a User onto its Posts
    posts = relationship(User,
                         backref=backref("posts",
                                         uselist=True,
                                         cascade='delete,all'))

    def __init__(self, text, author_id):
        self.text = text
        self.date_posted = datetime.datetime.now()
        self.author_id = author_id

    def __repr__(self):
        return '<title {}>'.format(self.text)
