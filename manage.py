"""Module with application entry point."""
from os import getenv
from flask import jsonify
from flask_marshmallow import Marshmallow
from api.middlewares.token_required import token_required

from main import create_app
from config import config


# get flask config name from env or default to production config
config_name = getenv('FLASK_ENV', default='production')

# create application object
app = create_app(config[config_name])

# create marshmallow object to handle serialization
ma = Marshmallow()


@app.route('/')
@token_required
def index():
    """Process / routes and returns 'Welcome to the AM api' as json."""
    return jsonify(dict(message='Welcome to the AM api'))


if __name__ == '__main__':
    app.run()
