from flask import Blueprint
from flask_restful import Api
from product.resources import ProductsListResource, ProductResource

product_bp = Blueprint('product', __name__)
api = Api(product_bp)

api.add_resource(ProductsListResource, '/products')
api.add_resource(ProductResource, '/products/<string:id>')
