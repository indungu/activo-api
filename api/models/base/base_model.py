"""Module for Base Model"""

import uuid

from ..model_operations import ModelOperations
from ..database import db


class BaseModel(db.Model, ModelOperations):
    """ Base model """

    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True)
    deleted = db.Column(db.Boolean, nullable=True, default=False)
