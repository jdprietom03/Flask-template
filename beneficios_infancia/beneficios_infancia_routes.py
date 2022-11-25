from flask import Blueprint
from flask_restful import Api
from beneficios_infancia.resources import BeneficiosInfanciaListResource, BeneficioInfanciaResource

beneficio_infancia_bp = Blueprint('beneficio_infancia', __name__)
api = Api(beneficio_infancia_bp)

api.add_resource(BeneficiosInfanciaListResource, '/beneficios_infancia')
api.add_resource(BeneficioInfanciaResource, '/beneficios_infancia/<string:id>')
