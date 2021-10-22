from functools import wraps
from flask import request, jsonify
import jwt
from ..routes import Config


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return jsonify({"message": 'Token is missing'}), 403
        try:
            data = jwt.decode(token, Config.SECRET_KEY)
        except Exception as error:
            return jsonify({"message": 'Token is missing or is invalid'}), 403
        return f(*args, **kwargs)
    return decorated


