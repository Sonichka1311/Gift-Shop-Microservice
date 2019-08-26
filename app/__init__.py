from flask import Flask
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


def create_app(testing_config=None):
    app = Flask(__name__)
    if testing_config is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    else:
        app.config.from_object(testing_config)
    from app.handlers import app_blueprint
    app.register_blueprint(app_blueprint)

    database.init_app(app)

    return app








