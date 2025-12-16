#!/usr/bin/env python3

from fastapi.testclient import TestClient

# import the FastAPI app
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to the Randomizer API'}
