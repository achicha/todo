import os
from flask import Flask
from .database import db
from flask_login import LoginManager


def create_app():
    # create the application object
    app = Flask(__name__)
    # app.config.from_object(os.environ['APP_SETTINGS'])
    app.config.from_object('config.DevConfig')
    login_manager = LoginManager()
    login_manager.init_app(app)
    db.init_app(app)
    # with app.test_request_context():
    #     db.create_all()

    from app.todo_list.controllers import bp_todo
    from app.login.controllers import bp_users

    app.register_blueprint(bp_todo)
    app.register_blueprint(bp_users)

    from .login.models import User

    login_manager.login_view = "users.login"

    # load user from DB and store it to the session
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()

    return app
