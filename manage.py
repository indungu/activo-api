from os import getenv as env
from flask import jsonify
from flask_script import Manager
from main import create_app
from config import config
from api.utilities.token_required import token_required

configuration = config[env('ENV') or 'development']
app = create_app(configuration)
manager = Manager(app)


@app.route('/')
@token_required
def index():
    """Process / routes and returns 'Welcome to the AM api' as json"""

    return jsonify(dict(message='Welcome to the AM api'))

if __name__ == '__main__':
    manager.run()