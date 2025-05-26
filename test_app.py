import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Cloud DevOps Automation" in response.data
    assert response.content_type == 'text/html; charset=utf-8'
