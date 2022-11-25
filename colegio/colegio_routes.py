from flask import Blueprint
from flask_restful import Api
from colegio.resources import ColegiosListResource, ColegioResource

colegio_bp = Blueprint('colegio', __name__)
api = Api(colegio_bp)

api.add_resource(ColegiosListResource, '/colegios')
api.add_resource(ColegioResource, '/colegios/<string:id>')
