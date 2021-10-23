from flask import json, request
from .fixtures.context import client

def test_endpoint_delete_users(client):
    response = client.delete('http://127.0.0.1:5000/users/1')
    assert response.status_code == 401
    assert b'"token is missing"' in response.data

def test_endpoint_update_users(client):
    response = client.put('http://127.0.0.1:5000/users/1')
    assert response.status_code == 401
    assert b'"token is missing"' in response.data
