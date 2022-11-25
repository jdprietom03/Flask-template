
from flask import render_template, make_response, request, redirect
from flask_restful import Resource
from database.ciudadanos_repository import CiudadanoRepository
from database.localidades_repository import LocalidadRepository
from database.sociales_repository import SocialRepository
from database.colegios_repository import ColegioRepository
import json
import plotly
import plotly.express as px
import pandas as pd

from model.Ciudadano import Ciudadano
from model.Social import Social


from threading import Thread

ciudadano_repository = CiudadanoRepository()
social_repository = SocialRepository()
colegio_repository = ColegioRepository()
localidad_repository = LocalidadRepository()


def create_graph_data(ciudadanos, colegios, localidades):
    beneficios_localidad = { localidad.Id: 0 for localidad in localidades  }
    beneficios_colegio = { colegio.Id: 0 for colegio in colegios  }
    beneficios_estrato = {}
    total_beneficios = 0


    for persona in ciudadanos:
        if persona.BPPS == "T" or persona.BPPI == "T":
            total_beneficios += 1

            if persona.Localidad not in beneficios_localidad:
                beneficios_localidad[persona.Localidad] = 0

            if persona.Colegio not in beneficios_colegio:
                beneficios_colegio[persona.Colegio] = 0

            if persona.Indicador not in beneficios_estrato:
                beneficios_estrato[persona.Indicador] = 0

            beneficios_localidad[persona.Localidad] += 1
            beneficios_colegio[persona.Colegio] += 1
            beneficios_estrato[persona.Indicador] += 1

    localidad_bar = {}
    localidad_chart = {}
    for i in beneficios_localidad.keys():
        if total_beneficios == 0: break
        localidad_chart[f"Localidad {i}"] = round(
            beneficios_localidad[i] * 100 / total_beneficios, 2)
        localidad_bar[f"Localidad {i}"] = beneficios_localidad[i]


    colegio_bar = {}
    colegio_chart = {}
    for i in beneficios_colegio.keys():
        if total_beneficios == 0: break
        colegio_chart[f"Colegio {i}"] = round(
            beneficios_colegio[i] * 100 / total_beneficios, 2)
        colegio_bar[f"Colegio {i}"] = beneficios_colegio[i]

    estrato_bar = {}
    estrato_chart = {}
    for i in range(len(beneficios_estrato)):
        if total_beneficios == 0: break
        estrato_chart[f"Estrato {i}"] = round(
            beneficios_estrato[i] * 100 / total_beneficios, 2)
        estrato_bar[f"Estrato {i}"] = beneficios_estrato[i]


    return {
        "pie": [
            localidad_chart, colegio_chart, estrato_chart
        ],
        "bar": [localidad_bar, colegio_bar, estrato_bar]
    }


class BeneficiosEconomicosListResource(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}

        ciudadanos = ciudadano_repository.filter_by_BPPS("T")
        social = social_repository.get_all()

        return make_response(render_template('beneficios_economicos.html', ciudadanos=ciudadanos, social=social[0], size=len(ciudadanos)), 200, headers)

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


class BeneficioEconomicoResource(Resource):
    def get(self, id):
        headers = {'Content-Type': 'text/html'}

        ciudadano = ciudadano_repository.get(id)

        return make_response(render_template('ciuadano.html', ciudadano=ciudadano), 200, headers)

    def put(self, id):
        headers = {'Content-Type': 'application/json'}
        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        [disponibles, asignados] = ciudadano_repository.set_beneficios_sociales(
            data["Total"])

        social_repository.update(Social({
            "Disponibles": disponibles,
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


class GraphResource(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}

        ciudadanos = ciudadano_repository.get_all()
        social = social_repository.get_all()
        colegios = set(colegio_repository.get_all())
        localidades = set(localidad_repository.get_all())

        data = create_graph_data(ciudadanos, colegios, localidades)
        pies = []
        tags = ["Localidad", "Colegio", "Estrato"]
        tagId = 0


        for element in data["pie"]:
            df = pd.DataFrame(element.items(), columns=[
                              tags[tagId], 'Porcentaje'])

            fig = px.pie(df, values='Porcentaje',
                         names=tags[tagId], title='Diagrama de torta ' + tags[tagId])
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            pies.append(graphJSON)
            tagId += 1

        bars = []
        tagId = 0

        for element in data["bar"]:
            data_sorted = list(element.items())
            data_sorted.sort(key=lambda x: int(x[0].split(" ")[1]))

            df = pd.DataFrame( data_sorted , columns=[
                              tags[tagId], 'Conteo'])

            fig = px.bar(df, x=tags[tagId], y='Conteo',
                         title='Diagrama de barras ' + tags[tagId])
            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            bars.append(graphJSON)
            tagId += 1

        return make_response(render_template('graph_social.html', bar1=bars[0], bar2=bars[1], bar3=bars[2], pie1=pies[0], pie2=pies[1], pie3=pies[2], social=social[0]), 200, headers)

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
