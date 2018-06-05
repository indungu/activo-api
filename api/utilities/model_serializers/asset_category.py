from marshmallow import fields, post_load, validate

from .base_schemas import BaseSchema
from api.models.asset_category import AssetCategory
from ..validators.string_validator import string_validator
from ..validators.string_length_validators import string_length_60_validator
from ..messages.error_messages import serialization_errors


class AssetCategorySchema(BaseSchema):
    """Asset category model schema"""

    name = fields.String(required=True,
                         validate=(string_length_60_validator,
                                   string_validator),
                         error_messages={
                             'required':
                             serialization_errors['field_required']})

    @post_load
    def create_asset_category(self, data):
        """Return asset category object after successful loading of data"""

        return AssetCategory(**data)
