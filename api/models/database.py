"""Database setup module."""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = None
session = None


def init_engine(uri, **kwargs):
    """Initialize and return the db engine."""
    global engine
    global Session
    engine = create_engine(uri, **kwargs)
    Session = sessionmaker()
    Session.configure(bind=engine)
    return engine


def get_engine():
    """Retrieve engine."""
    global engine
    return engine


def mk_session():
    """Create db session."""
    global Session
    session = Session()
    return session


Base = declarative_base()
metadata = MetaData()
