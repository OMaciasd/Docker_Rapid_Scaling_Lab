# myapp/app/routes.py
from flask import Blueprint

blueprint = Blueprint('app', __name__)


@blueprint.route('/app')
def app_route():
    return "This is the app route!"
