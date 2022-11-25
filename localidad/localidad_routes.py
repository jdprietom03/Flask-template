from flask import Blueprint
from flask_restful import Api
from localidad.resources import LocalidadesListResource, LocalidadResource

localidad_bp = Blueprint('localidad', __name__)
api = Api(localidad_bp)

api.add_resource(LocalidadesListResource, '/localidades')
api.add_resource(LocalidadResource, '/localidades/<string:id>')
