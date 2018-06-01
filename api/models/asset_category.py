from .base.auditable_model import AuditableBaseModel
from .database import db


class AssetCategory(AuditableBaseModel):
    """
    Model for asset categories
    """

    __tablename__ = 'asset_categories'

    name = db.Column(db.String(60), nullable=False)
    assets = db.relationship('Asset', backref='asset_category',
                             cascade='save-update, delete', lazy=True)
    attributes = db.relationship('Attribute', backref='asset_category',
                                 cascade='save-update, delete', lazy=True)

    def __repr__(self):
        return '<AssetCategory {}>'.format(self.name)
