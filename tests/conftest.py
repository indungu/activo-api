import pytest

from main import create_app
from config import config
from api.models.database import db as _db
from api.models.user import User
from api.models.asset_category import AssetCategory

config_name = 'testing'


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """

    _app = create_app(config[config_name])

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()


@pytest.fixture(scope='module')
def new_user(app):
    params = {
      'id': '1',
      'name': 'Ayo',
      'email': 'testemail@gmail.com',
      'image_url': 'http://some_url'
    }
    user = User(**params)
    return user


@pytest.fixture(scope='module')
def new_asset_category(app):
    params = {
      'name': 'Laptop'
    }
    asset_category = AssetCategory(**params)
    return asset_category


@pytest.fixture(scope='session')
def init_db(app):
    _db.create_all()
    yield _db
    _db.drop_all()

