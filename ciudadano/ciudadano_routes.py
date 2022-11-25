from flask import Blueprint
from flask_restful import Api
from ciudadano.resources import CiudadanosListResource, CiudadanoResource

ciudadano_bp = Blueprint('ciudadano', __name__)
api = Api(ciudadano_bp)

api.add_resource(CiudadanosListResource, '/ciudadanos')
api.add_resource(CiudadanoResource, '/ciudadanos/<string:id>')
