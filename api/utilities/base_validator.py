from flask import Blueprint, jsonify

middleware = Blueprint('middleware', __name__)


class ValidationError(Exception):
    status_code = 400

    def __init__(self, error, status_code=None):
        Exception.__init__(self)
        self.error = error
        self.error['status'] = 'Failure'
        self.error['message'] = error['message']

        if status_code is not None:
            self.error['status_code'] = status_code

    def to_dict(self):
        return self.error


@middleware.app_errorhandler(ValidationError)
def handle_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
