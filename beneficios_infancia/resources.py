
from flask import render_template, make_response, request, redirect
from flask_restful import Resource
from database.ciudadanos_repository import CiudadanoRepository
from database.infancias_repository import InfanciaRepository
import json

from model.Ciudadano import Ciudadano
from model.Infancia import Infancia

ciudadano_repository = CiudadanoRepository()
infancia_repository = InfanciaRepository()


class BeneficiosInfanciaListResource(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}

        ciudadanos = ciudadano_repository.filter_by_BPPI("T")
        infancia = infancia_repository.get_all()

        return make_response(render_template('beneficios_infancia.html', ciudadanos=ciudadanos, infancia = infancia[0], size = len(ciudadanos)), 200, headers)

    def post(self):
        headers = {'Content-Type': 'application/json'}

        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        ciudadano = ciudadano_repository.create(Ciudadano(data))

        response = {
            "message": "ciudadano creado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)


class BeneficioInfanciaResource(Resource):
    def get(self, id):
        headers = {'Content-Type': 'text/html'}

        ciudadano = ciudadano_repository.get(id)

        return make_response(render_template('ciuadano.html', ciudadano=ciudadano), 200, headers)

    def put(self, id):
        headers = {'Content-Type': 'application/json'}
        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        [ disponibles, asignados ] = ciudadano_repository.set_beneficios_infancia( data["Total"] )

        infancia_repository.update(Infancia({
            "Disponibles": disponibles ,
            "Asignados": asignados
        }), id)

        response = {
            "message": "Beneficio economico actualizado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)

    def delete(self, id):
        headers = {'Content-Type': 'application/json'}
        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        ciudadano_repository.update(Ciudadano(data), id)

        response = {
            "message": "Beneficio economico actualizado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)
