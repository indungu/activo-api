"""Module for application factory."""
from os import getenv
from flask import Flask
from flask_migrate import Migrate

from config import config
from api.models.database import db

config_name = getenv('FLASK_ENV', default='production')


def create_app(config=config[config_name]):
    """Return app object given config object."""
    app = Flask(__name__)
    app.config.from_object(config)

    # bind app to db
    db.init_app(app)

    # import all models
    from api.models.user import User

    # initialize migration scripts
    migrate = Migrate(app, db)

    return app
