from flask import json, request
from .fixtures.context import client

def test_signup_user(client):
    response = client.post('http://127.0.0.1:5000/auth/signup',
    json={
        "firstName": "Marcos",
        "lastName": "Valente",
        "birthdate": "1999-11-13",
        "addresses": [
            {
                "street": "Rua São Paulo",
                "number": 100,
                "city": "Belo Horizonte"
            },
            {
                "street": "Rua Sergipe",
                "number": 110,
                "city": "Belo Horizonte"
            }
        ],
    })
    assert response.status_code == 201
    assert b'registered successfully' in response.data
    assert b'token' in response.data

def test_signup_user_quando_payload_e_invalido(client):
    response = client.post('http://127.0.0.1:5000/auth/signup',
    json={
        "firstName": "Marcos",
        "Invalid": "Valente",
        "birthdate": "1999-11-13",
        "addresses": [
            {
                "street": "Rua São Paulo",
                "number": 100,
                "city": "Belo Horizonte"
            },
            {
                "street": "Rua Sergipe",
                "number": 110,
                "city": "Belo Horizonte"
            }
        ],
    })
    assert response.status_code == 400
    assert b'\'lastName\' is missing or incorrect' in response.data

def test_signup_user_quando_payload_param_de_addresses_e_invalido(client):
    response = client.post('http://127.0.0.1:5000/auth/signup',
    json={
        "firstName": "Marcos",
        "lastName": "Valente",
        "birthdate": "1999-11-13",
        "addresses": [
            {
                "invalid": "Rua São Paulo",
                "number": 100,
                "city": "Belo Horizonte"
            },
            {
                "street": "Rua Sergipe",
                "number": 110,
                "city": "Belo Horizonte"
            }
        ],
    })
    assert response.status_code == 400
    assert b'param \'street\' is missing or is incorrect' in response.data
