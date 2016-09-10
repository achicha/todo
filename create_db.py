from app.database import db
from app import create_app

myapp = create_app()

with myapp.app_context():
    db.create_all()
