from flask import Flask


def initialize_errorhandlers(application):
    '''
    Initialize error handlers
    '''
    from api.middlewares.base_validator import middleware_blueprint
    application.register_blueprint(middleware_blueprint)


def create_app(config):
    """
    Takes a config object and create an instance of the app with the config
    """

    app = Flask(__name__)
    app.config.from_object(config)
    initialize_errorhandlers(app)

    return app
