from .database import db
from uuid import uuid4

class ModelOperations(object):
    def save(self):
        """
        Save a model instance

        :return: Model instance
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
    def get_one(cls, id):
        """
        return entries by id
        """
        return cls.query.get(id)

    def delete(self):
        """
        Delete a model instance.
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        """
        return all database entries
        """
        all_entries = cls.query.all()
        db.session.commit()
        return all_entries
 
    @classmethod
    def count(cls):
        """
        return total entries in the database
        """
        counts = cls.query.count()
        db.session.commit()
        return counts