from flask import json, request
from .fixtures.context import client


def test_endpoint_get_users_deve_retornar_401_quando_sem_token_nos_headers(client):
    response = client.get('http://127.0.0.1:5000/users')
    assert response.status_code == 401
    assert b'"token is missing"' in response.data

def test_endpoint_delete_users_deve_retornar_401_quando_sem_token_nos_headers(client):
    response = client.delete('http://127.0.0.1:5000/users/1')
    assert response.status_code == 401
    assert b'"token is missing"' in response.data

def test_endpoint_put_users_deve_retornar_401_quando_sem_token_nos_headers(client):
    response = client.put('http://127.0.0.1:5000/users/1')
    assert response.status_code == 401
    assert b'"token is missing"' in response.data
