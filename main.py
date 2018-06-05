"""Module for application factory."""
from os import getenv
from flask import Flask
from flask_migrate import Migrate
from flask_restplus import Api

api = Api()

from config import config
from api.models.database import db

config_name = getenv('FLASK_ENV', default='production')


def initialize_errorhandlers(application):
    ''' Initialize error handlers '''
    from api.middlewares.base_validator import middleware_blueprint
    application.register_blueprint(middleware_blueprint)


def create_app(config=config[config_name]):
    """Return app object given config object."""
    app = Flask(__name__)
    app.config.from_object(config)

    # initialize error handlers
    initialize_errorhandlers(app)

    # bind app to db
    db.init_app(app)

    # bind flask_restplus to app
    api.init_app(app)

    # import all models
    from api.models import User, Asset, AssetCategory, Attribute

    # initialize migration scripts
    migrate = Migrate(app, db)

    return app
