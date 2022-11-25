
from flask import render_template, make_response, request, redirect
from flask_restful import Resource
from database.colegios_repository import ColegioRepository
import json

from model.Colegio import Colegio

colegio_repository = ColegioRepository()


class ColegiosListResource(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}

        colegios = colegio_repository.get_all()

        return make_response(render_template('colegios.html', colegios=colegios), 200, headers)

    def post(self):
        headers = {'Content-Type': 'application/json'}

        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        colegio = colegio_repository.create(colegio(data))

        response = {
            "message": "colegioo creado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)


class ColegioResource(Resource):
    def get(self, id):
        headers = {'Content-Type': 'text/html'}

        colegio = colegio_repository.get(id)

        return make_response(render_template('colegio.html', colegio=colegio), 200, headers)

    def put(self, id):
        headers = {'Content-Type': 'application/json'}
        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        colegio_repository.update(Colegio(data), id)

        response = {
            "message": "colegioo actualizado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)

    def delete(self, id):
        colegio_repository.delete(id)

        return redirect('/colegios/', code=200)
