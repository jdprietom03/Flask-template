from flask import Blueprint
from flask_restful import Api
from programa.resources import ProgramasListResource, ProgramaResource

programa_bp = Blueprint('programa', __name__)
api = Api(programa_bp)

api.add_resource(ProgramasListResource, '/programas')
api.add_resource(ProgramaResource, '/programas/<string:id>')
