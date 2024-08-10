import pytest
from myapp.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_route(client):
    """Verifica que la ruta /app responde con el texto esperado."""
    response = client.get('/app')
    assert response.status_code == 200
    assert b'This is the app route!' in response.data
