from os import getenv as env
from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config(object):
    """App base configuration"""

    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    """App production configuration"""
    pass

class DevelopmentConfig(Config):
    """App development configuration"""
    DEBUG = True

class TestingConfig(Config):
    """App testing configuration"""
    TESTING = True

config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig,
  'testing': ProductionConfig
}
