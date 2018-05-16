from datetime import datetime
from ..database import db


class AuditableModel(db.Model):
    """ Auditable model """

    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, ondelete=datetime.utcnow)
    created_by = db.Column(db.String, nullable=True)
    updated_by = db.Column(db.String, nullable=True)
    deleted_by = db.Column(db.String, nullable=True)
