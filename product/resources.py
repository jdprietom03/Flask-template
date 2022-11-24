
from flask import render_template, make_response, request, redirect
from flask_restful import Resource
from database.products_repository import ProductRepository
import json

from model.Product import Product

product_repository = ProductRepository()


class ProductsListResource(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}

        products = product_repository.get_all()

        return make_response(render_template('products.html', products=products), 200, headers)

    def post(self):
        headers = {'Content-Type': 'application/json'}

        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        product = product_repository.create(Product(data))

        response = {
            "message": "Producto actualizado correctamente",
        }

        return make_response(json.dumps(response), 200, headers)


class ProductResource(Resource):
    def get(self, id):
        headers = {'Content-Type': 'text/html'}

        product = product_repository.get(id)

        return make_response(render_template('product.html', product=product), 200, headers)

    def put(self, id):
        headers = {'Content-Type': 'application/json'}
        # Get the data from the request
        data = request.data.decode()
        data = json.loads(data)

        product_repository.update(Product(data), id)

        response = {
            "message": "Producto actualizado correctamente",
        }


        return make_response(json.dumps(response), 200, headers)

    def delete(self, id):
        product_repository.delete(id)

        return redirect('/products/', code=200)
