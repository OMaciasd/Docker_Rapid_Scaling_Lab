# test_app.py

import pytest
from flask import Flask
from myapp.app import blueprint

# Configura una aplicación Flask de prueba


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(blueprint)

    with app.test_client() as client:
        yield client


def test_app_route(client):
    """Verifica que la ruta /app responde con el texto esperado."""
    response = client.get('/app')
    assert response.status_code == 200
    assert b'This is the app route!' in response.data
