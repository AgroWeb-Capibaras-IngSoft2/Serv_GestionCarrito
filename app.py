from flask import Flask
from Infraestructure.Routes import bp
from flask_cors import CORS
from flasgger import Swagger
#Usamos Prometheus para la implementación de la observabilidad
from prometheus_client import generate_latest,CONTENT_TYPE_LATEST
from Infraestructure.metrics import REQUEST_COUNT, REQUEST_LATENCY, ERROR_COUNT

app = Flask(__name__)
CORS(app, origins=["http://localhost:5174"])  # Allow CORS for the specified origin

# Configuración de Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Servicio de Gestión de Carrito de Compras",
        "description": "API REST para la gestión completa de carritos de compras con arquitectura limpia",
        "version": "1.0.0",
        "contact": {
            "name": "AgroWeb-Capibaras-IngSoft2",
            "url": "https://github.com/AgroWeb-Capibaras-IngSoft2/GestionCarrito"
        }
    },
    "host": "localhost:5003",
    "basePath": "/",
    "schemes": ["http"],
    "consumes": ["application/json"],
    "produces": ["application/json"]
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

app.register_blueprint(bp)

@app.route('/metrics')
def metrics():
    return generate_latest(),200,{'Content-Type':CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(debug=True, port=5003)  # Run on port 5001 for Serv_Usuarios