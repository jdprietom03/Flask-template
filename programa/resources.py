
from flask import render_template, make_response, request, redirect
from flask_restful import Resource
from database.programas_repository import ProgramaRepository
import json

from model.Programa import Programa

programa_repository = ProgramaRepository()


class ProgramasListResource(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}

        programas = programa_repository.get_all()

        return make_response(render_template('programas.html', programas=programas), 200, headers)

    def post(self):
        headers = {'Content-Type': 'application/json'}

        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        programa = programa_repository.create(Programa(data))

        response = {
            "message": "programa creado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)


class ProgramaResource(Resource):
    def get(self, id):
        headers = {'Content-Type': 'text/html'}

        programa = programa_repository.get(id)

        return make_response(render_template('ciuadano.html', programa=programa), 200, headers)

    def put(self, id):
        headers = {'Content-Type': 'application/json'}
        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        programa_repository.update(Programa(data), id)

        response = {
            "message": "Programa actualizado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)

    def delete(self, id):
        programa_repository.delete(id)

        return redirect('/programas/', code=200)
