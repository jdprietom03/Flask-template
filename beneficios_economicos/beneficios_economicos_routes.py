from flask import Blueprint
from flask_restful import Api
from beneficios_economicos.resources import BeneficiosEconomicosListResource, BeneficioEconomicoResource, GraphResource

beneficio_economico_bp = Blueprint('beneficio_economico', __name__)
api = Api(beneficio_economico_bp)

api.add_resource(BeneficiosEconomicosListResource, '/beneficios_economicos')
api.add_resource(BeneficioEconomicoResource, '/beneficios_economicos/<string:id>')
api.add_resource(GraphResource, '/graph/beneficios')
