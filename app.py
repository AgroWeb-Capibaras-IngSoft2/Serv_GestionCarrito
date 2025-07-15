from flask import Flask
from Infraestructure.Routes import bp
from flask_cors import CORS
#Usamos Prometheus para la implementación de la observabilidad
from prometheus_client import generate_latest,CONTENT_TYPE_LATEST
from Infraestructure.metrics import REQUEST_COUNT, REQUEST_LATENCY, ERROR_COUNT

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])  # Allow CORS for the specified origin

app.register_blueprint(bp)

@app.route('/metrics')
def metrics():
    return generate_latest(),200,{'Content-Type':CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(debug=True, port=5003)  # Run on port 5001 for Serv_Usuarios