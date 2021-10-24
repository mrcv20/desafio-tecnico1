from functools import wraps
from flask import request, jsonify
import jwt
from ..routes import Config


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({"message": "token is missing"}), 401
        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        except Exception as error:
            return jsonify({"message": f'Token is invalid'}), 401
        return f(*args, **kwargs)
    return decorated


