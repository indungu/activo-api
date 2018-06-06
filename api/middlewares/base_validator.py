"""Module for Validation error and error handler"""

from flask import Blueprint, jsonify
from main import api

middleware_blueprint = Blueprint('middleware', __name__)


class ValidationError(Exception):
    """Base Validation class for handling validation errors"""

    def __init__(self, error, status_code=None):
        Exception.__init__(self)
        self.status_code = 400
        self.error = error
        self.error['status'] = 'Failure'
        self.error['message'] = error['message']

        if status_code is not None:
            self.status_code = status_code
            self.error['status_code'] = status_code
        else:
            self.error['status_code'] = self.status_code

    def to_dict(self):
        return self.error


@api.errorhandler(ValidationError)
@middleware_blueprint.app_errorhandler(ValidationError)
def handle_exception(error):
    """Error handler called when a ValidationError Exception is raised"""

    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
