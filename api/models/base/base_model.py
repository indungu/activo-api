import uuid

from ..database import db


class BaseModel(db.Model):
    """ Base model """

    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4())
