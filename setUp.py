import app


app = app.create_app()

from app import database


with app.app_context():
    database.create_all()
