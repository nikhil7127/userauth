from flask import request,jsonify
from models import Database
from functools import wraps
import jwt

db = Database()

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'})
        try:
            data = jwt.decode(token, '65aea63a16bf4e1ba415f0215cbfee55',algorithms=['HS256'])
        except jwt.InvalidTokenError:
            return {"message":'Invalid token. Please log in again.'}
        except:
            return jsonify({'Message': 'Invalid token'})
        return func(*args, **kwargs)
    return decorated
