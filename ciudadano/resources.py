
from flask import render_template, make_response, request, redirect
from flask_restful import Resource
from database.ciudadanos_repository import CiudadanoRepository
import json

from model.Ciudadano import Ciudadano

ciudadano_repository = CiudadanoRepository()


class CiudadanosListResource(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}

        ciudadanos = ciudadano_repository.get_all()

        return make_response(render_template('ciudadanos.html', ciudadanos=ciudadanos), 200, headers)

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


class CiudadanoResource(Resource):
    def get(self, id):
        headers = {'Content-Type': 'text/html'}

        ciudadano = ciudadano_repository.get(id)

        return make_response(render_template('ciuadano.html', ciudadano=ciudadano), 200, headers)

    def put(self, id):
        headers = {'Content-Type': 'application/json'}
        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        ciudadano_repository.update(Ciudadano(data), id)

        response = {
            "message": "Ciudadano actualizado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)

    def delete(self, id):
        ciudadano_repository.delete(id)

        return redirect('/ciudadanos/', code=200)
