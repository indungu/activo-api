from flask import Flask

def create_app(config):
    """Takes a config object and create an instance of the app with the config"""

    app = Flask(__name__)
    app.config.from_object(config)

    return app
