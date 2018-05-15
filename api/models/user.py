"""Module for User model."""
from sqlalchemy import Column, Unicode, String
from uuid import uuid4

from .database import Base


class User(Base):
    """Class for user db table."""

    __tablename__ = 'users'
    id = Column(String(255),
                primary_key=True,
                default=uuid4())
    name = Column(Unicode(32))
    email = Column(String, unique=True)
