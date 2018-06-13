from .base.auditable_model import AuditableBaseModel
from .database import db


class Asset(AuditableBaseModel):
    """
    Model for assets
    """
    tag = db.Column(db.String(60), nullable=False)
    serial = db.Column(db.String(60), nullable=False)
    asset_category_id = db.Column(db.String,
                                  db.ForeignKey('asset_categories.id'),
                                  nullable=False)

    def get_child_relationships(self):
        """
        Method to get all child relationships a model has. Overide in the
        subclass if the model has child models.
        """
        return None

    def __repr__(self):
        return '<Asset {}>'.format(self.tag)
