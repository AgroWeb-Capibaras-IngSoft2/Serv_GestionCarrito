from flask import Flask
from Infraestructure.Routes import bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])  # Allow CORS for the specified origin

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True, port=5003)  # Run on port 5001 for Serv_Usuarios