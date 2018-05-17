"""Module for User model."""

from .database import db
from .base.base_model import BaseModel
from .model_operations import ModelOperations


class User(BaseModel, ModelOperations):
    """Class for user db table."""
    
    __tablename__ = 'users'
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    image_url = db.Column(db.String)
