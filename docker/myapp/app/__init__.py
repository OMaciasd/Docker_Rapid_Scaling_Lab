from flask import (
    Flask,
    Blueprint
)

# Define el Blueprint aquí
blueprint = Blueprint('app', __name__)


def create_app():
    app = Flask(__name__)

    from . import routes
    routes.init_app(app)

    return app
