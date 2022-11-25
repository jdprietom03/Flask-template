from flask import Flask
from product.product_routes import product_bp
from colegio.colegio_routes import colegio_bp
from localidad.localidad_routes import localidad_bp
from ciudadano.ciudadano_routes import ciudadano_bp
from programa.programa_routes import programa_bp
from beneficios_economicos.beneficios_economicos_routes import beneficio_economico_bp
from beneficios_infancia.beneficios_infancia_routes import beneficio_infancia_bp
from home.home_routes import home_bp

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'

app.register_blueprint(product_bp)
app.register_blueprint(colegio_bp)
app.register_blueprint(localidad_bp)
app.register_blueprint(ciudadano_bp)
app.register_blueprint(programa_bp)
app.register_blueprint(beneficio_economico_bp)
app.register_blueprint(beneficio_infancia_bp)
app.register_blueprint(home_bp)


if __name__ == '__main__':
    app.run(debug=True, port = 8080)