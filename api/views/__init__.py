from flask import Blueprint
from flask_restplus import Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
