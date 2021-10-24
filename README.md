
# API para cadastro de usuários com JWT

## Sobre

API para cadastro de usuários 

Tecnologias usadas:
- Python
- Flask
- SQLite3

## Preparando o ambiente virtual
Na pasta raiz digite os comandos
```
pip install virtualenv

virtualenv ./env

source env/bin/activate
```

## Instalando as dependências
No diretório raiz, instale as bibliotecas com o pip
```
pip install -r requirements.txt
```

## Rodando os testes
No diretório raiz, digite os comandos:

```
export FLASK_APP=server.py
export FLASK_ENV=testing
pytest -v tests/
```

## Criação das tabelas e do banco de dados
```
    Base.metadata.create_all(engine)
```

## Subindo a API
```
export FLASK_APP=server.py
export FLASK_ENV=development
flask run
```

- Endereço da documentação: http://localhost:5000/swagger/

