from flask import json, request
from .fixtures.context import client

def test_endpoint_get_users_quando_token_valido_deve_retornar_200_e_listar_usuarios(client):
    headers = {'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5fQ.H3zbe6k9vZsVlrIz9chCiisHwaHv6gh5cA0ZCokmwyA'}
    response = client.get('http://127.0.0.1:5000/users', headers=headers)
    assert response.status_code == 200
    assert b'"users"' in response.data

def test_endpoint_update_users_quando_token_valido_deve_retornar_200_e_atualizar_usuario(client):
    headers = {'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5fQ.H3zbe6k9vZsVlrIz9chCiisHwaHv6gh5cA0ZCokmwyA'}
    response = client.put('http://127.0.0.1:5000/users/1', headers=headers, 
    json={
        "firstName": "Marcos",
        "lastName": "Valente",
        "birthdate": "1999-11-13",
    })
    assert response.status_code == 200
    assert b'User updated successfully' in response.data

def test_endpoint_delete_users_quando_token_valido_deve_retornar_200_e_deletar_usuario(client):
    headers = {'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5fQ.H3zbe6k9vZsVlrIz9chCiisHwaHv6gh5cA0ZCokmwyA'}
    response = client.delete('http://127.0.0.1:5000/users/1', headers=headers)
    assert response.status_code == 200
    assert b'User deleted successfully' in response.data


def test_endpoint_get_users_quando_sem_token_nos_headers_deve_retornar_401(client):
    response = client.get('http://127.0.0.1:5000/users')
    assert response.status_code == 401
    assert b'"token is missing"' in response.data

def test_endpoint_delete_users_quando_sem_token_nos_headers_deve_retornar_401(client):
    response = client.delete('http://127.0.0.1:5000/users/1')
    assert response.status_code == 401
    assert b'"token is missing"' in response.data

def test_endpoint_update_users_quando_sem_token_nos_headers_deve_retornar_401(client):
    response = client.put('http://127.0.0.1:5000/users/1')
    assert response.status_code == 401
    assert b'"token is missing"' in response.data
