from flask import Flask
from product.product_routes import product_bp

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'

app.register_blueprint(product_bp)


if __name__ == '__main__':
    app.run(debug=True, port = 8080)