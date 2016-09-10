import os

from flask_migrate import Migrate
from flask_script import Manager, Server

from app import create_app
from app.database import db


app = create_app()
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevConfig')
migrate = Migrate(app, db)  # create migration instance
manager = Manager(app)  # create Manager instance
manager.add_command("runserver", Server(
    host='0.0.0.0',
    use_debugger=True,
    use_reloader=True
))

if __name__ == '__main__':
    manager.run()
