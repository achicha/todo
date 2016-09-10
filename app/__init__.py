import os
from flask import Flask
from .database import db


def create_app():
    app = Flask(__name__)
    # app.config.from_object(os.environ['APP_SETTINGS'])
    app.config.from_object('config.DevConfig')
    db.init_app(app)
    # with app.test_request_context():
    #     db.create_all()

    from app.todo_list.controllers import bp_todo

    app.register_blueprint(bp_todo)

    return app
