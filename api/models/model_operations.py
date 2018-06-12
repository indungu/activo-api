"""Module for generic model operations mixin."""
from .database import db
from ..utilities.validators.delete_validator import delete_validator
from ..middlewares.base_validator import ValidationError
from ..utilities.messages.error_messages import database_errors


class ModelOperations(object):
    """Mixin class with generic model operations."""
    def save(self):
        """
        Save a model instance
        """
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, **kwargs):
        """
        update entries
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        db.session.commit()

    @classmethod
    def get(cls, id):
        """
        return entries by id
        """
        return cls.query.get(id)

    def get_child_relationships(self):
        """
        Method to get all child relationships a model has.
        This is used to ascertain if a model has relationship(s) or
        not when validating delete operation.
        It must be overridden in subclasses and takes no argument.
        :return None if there are no child relationships.
        A tuple of all child relationships eg (self.relationship_field1,
        self.relationship_field2)
        """
        raise NotImplementedError("The get_relationships method must be overridden in all child model classes") #noqa

    def delete(self):
        """
        Soft delete a model instance.
        """
        relationships = self.get_child_relationships()
        if delete_validator(relationships):
            self.deleted = True
            db.session.add(self)
            db.session.commit()
        else:
            raise ValidationError(dict(
                message=database_errors['model_delete_children'].format(relationships)),
                                  status_code=403)

    @classmethod
    def _query(cls):
        """
        return all database entries
        """
        all_entries = cls.query
        return all_entries

    @classmethod
    def count(cls):
        """
        return total entries in the database
        """
        counts = cls.query.count()
        return counts
