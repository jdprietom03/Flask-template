from flask import Blueprint, make_response, render_template
from flask_restful import Api, Resource

class Home(Resource):
    def get(self):
        return make_response(render_template('index.html'), 200)


home_bp = Blueprint('home', __name__)
api = Api(home_bp)

api.add_resource(Home, '/')
