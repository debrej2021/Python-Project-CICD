# test_simple_python.py

import pytest
from simple_python import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}
