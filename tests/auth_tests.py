from flask import json, request
from .fixtures.context import client

def test_signup_user(client):
    response = client.post('http://127.0.0.1:5000/auth/signup')
    assert response.status_code == 201
    assert b'"token"' in response.data

def test_login_user(client):
    response = client.post('http://127.0.0.1:5000/auth/login')
    assert response.status_code == 200
    assert b'"token"' in response.data
