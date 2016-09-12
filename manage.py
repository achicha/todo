import os
import unittest
import coverage
import datetime

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app.login.models import User

from app import create_app
from app.database import db

"""
how to use migrations:
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade

run tests:
python3 manage.py test/cov
"""


app = create_app()
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevConfig')
migrate = Migrate(app, db)  # create migration instance
manager = Manager(app)  # create Manager instance

manager.add_command('db', MigrateCommand)  # migrations
manager.add_command("runserver", Server(
    host='0.0.0.0',
    use_debugger=True,
    use_reloader=True
))


@manager.command
def test():
    """Runs the tests without coverage."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    cov = coverage.coverage(branch=True, include='app/*', omit='*/__init__.py')
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.erase()


@manager.command
def create_db():
    """Creates the db tables."""
    with app.app_context():
        db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    with app.app_context():
        db.drop_all()


@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(
        name='admin',
        email="ad@min.com",
        password="admin",
        admin=True,
        confirmed=True,
        confirmed_on=datetime.datetime.now())
    )
    db.session.commit()

if __name__ == '__main__':
    manager.run()
