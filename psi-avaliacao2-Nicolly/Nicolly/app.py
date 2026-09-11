# app.py — Oficina de Conserto (versão inicial)
from flask import Flask
from blueprints.auth import auth_bp
from blueprints.catalog import catalog_bp
from blueprints.servicos import servicos_bp

app = Flask(__name__)
app.secret_key = "nico"

app.register_blueprint(auth_bp)
app.register_blueprint(catalog_bp)
app.register_blueprint(servicos_bp)

if __name__ == "__main__":
    app.run(debug=True)