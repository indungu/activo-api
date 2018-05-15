"""Module for User model."""
from uuid import uuid4

from .database import db


class User(db.Model):
    """Class for user db table."""

    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key=True, default=uuid4())
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
