
from flask import render_template, make_response, request, redirect
from flask_restful import Resource
from database.localidades_repository import LocalidadRepository
import json

from model.Localidad import Localidad

localidad_repository = LocalidadRepository()


class LocalidadesListResource(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}

        localidades = localidad_repository.get_all()

        return make_response(render_template('localidades.html', localidades=localidades), 200, headers)

    def post(self):
        headers = {'Content-Type': 'application/json'}

        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        localidad = localidad_repository.create(localidad(data))

        response = {
            "message": "localidado creado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)


class LocalidadResource(Resource):
    def get(self, id):
        headers = {'Content-Type': 'text/html'}

        localidad = localidad_repository.get(id)

        return make_response(render_template('localidad.html', localidad=localidad), 200, headers)

    def put(self, id):
        headers = {'Content-Type': 'application/json'}
        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        localidad_repository.update(Localidad(data), id)

        response = {
            "message": "localidado actualizado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)

    def delete(self, id):
        localidad_repository.delete(id)

        return redirect('/localidads/', code=200)
