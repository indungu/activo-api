from .database import db
from api.utilities.dynamic_filter import DynamicFilter


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
    def get(cls, id):
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
    def _query(cls, filter_condition):
        """
        Returns filtered database entries. It takes model class and
        filter_condition and returns database entries based on the filter
        condition, eg, User._query('name,like,john'). Apart from 'like', other
        comparators are eq(equal to), ne(not equal to), lt(less than),
        le(less than or equal to) gt(greater than), ge(greater than or equal to)
        :param filter_condition:
        :return: an array of filtered records
        """
        dynamic_filter = DynamicFilter(cls)
        return dynamic_filter.filter_query(filter_condition)

    @classmethod
    def count(cls):
        """
        Returns total entries in the database
        """
        counts = cls.query.count()
        return counts
