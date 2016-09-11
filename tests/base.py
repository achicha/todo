from flask_testing import TestCase

from app import create_app
from app.database import db

from app.todo_list.models import Post
from app.login.models import User


app = create_app()


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "ad@min.com", "admin"))
        db.session.add(
            Post("Test post", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
