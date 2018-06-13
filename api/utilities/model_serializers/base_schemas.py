""" Module for base marshmallow schema. """
from marshmallow import Schema, fields
from json import JSONDecodeError

from ..messages.error_messages import serialization_errors
from ...middlewares.base_validator import ValidationError


class BaseSchema(Schema):
    """Base marshmallow schema with common attributes."""
    id = fields.String(dump_only=True)
    deleted = fields.Boolean(dump_only=True)

    def load_json_into_schema(self, data):
        """Helper function to load raw json request data into schema"""

        try:
            data, errors = self.loads(data)
        except JSONDecodeError:
            raise ValidationError(
                dict(errors=serialization_errors['json_invalid'],
                     message='failed'), 400)
        if errors:
            raise ValidationError(dict(errors=errors,
                                       message='An error occurred'), 422)

        return data

    def load_object_into_schema(self, data):
        """Helper function to load python objects into schema"""

        try:
            data, errors = self.load(data)
        except KeyError as error:
            raise ValidationError(dict(errors=error,
                                       message='An error occurred'), 400)
        if errors:
            raise ValidationError(dict(errors=errors,
                                       message='An error occurred'), 422)

        return data


class AuditableBaseSchema(BaseSchema):
    """ Base marshmallow schema for auditable models. """
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
    created_by = fields.DateTime(dump_only=True)
    updated_by = fields.DateTime(dump_only=True)
    deleted_by = fields.DateTime(dump_only=True)
