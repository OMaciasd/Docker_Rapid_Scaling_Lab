# myapp/app/__init__.py
from flask import Flask
from .routes import blueprint  # Ahora importa blueprint desde routes


def create_app():
    app = Flask(__name__)

    # Registrar el Blueprint
    app.register_blueprint(blueprint)

    return app
