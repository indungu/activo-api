from .filter_functions import (
	like, is_equal, less_than, not_equal,
	greater_than, less_or_equal, greater_or_equal
)
from api.middlewares.base_validator import ValidationError


class DynamicFilter:
	"""
	A class that returns filtered database records
	"""

	def __init__(self, model):
		"""
		Constructor to initialize an instance of the class.
		:param model: the model class that will be using the methods of
		this class
		"""
		self.model = model
		self.query = model.query

	mapper = {
		'like': like,
		'eq': is_equal,
		'lt': less_than,
		'ne': not_equal,
		'gt': greater_than,
		'le': less_or_equal,
		'ge': greater_or_equal,
	}

	def filter_query(self, args):
		"""
		Returns filtered database entries.
		An example of filter_condition is: User._query('name,like,john').
		Apart from 'like', other comparators are
		eq(equal to), ne(not equal to), lt(less than), le(less than or equal to)
		gt(greater than), ge(greater than or equal to)
		:param filter_condition:
		:return: an array of filtered records

		"""
		raw_filters = args.getlist('where')
		result = self.query
		if not raw_filters:
			return self.query.all()

		for raw in raw_filters:
			try:
				key, op, value = raw.split(',', 3)
			except ValueError:
				raise ValidationError(dict(message='Invalid filter format:'
				'\'{}\'. Provide filter in the form: \'name,like,apple\''
				.format(raw)))

			column = getattr(self.model, key, None)
			if not column:
				raise ValidationError(dict(
					message='Invalid filter column: %s' % key))

			db_filter = self.mapper.get(op)
			result = result.filter(db_filter(column, value))
		return result
