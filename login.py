from flask import request
from flask_restful import Resource
from db import db
from hashlib import sha256
import jwt
from time import time


class Login(Resource):
    def get(self):
        data = request.args.to_dict()
        if data.get('password') and data.get('email') and data.get('key'):
            if data['key'] == 'e75774559e4c4532a313769f7294d70b':
                user = db.findUser(data['email'].strip())
                if user and  user[0] == sha256(data['password'].strip().encode()).hexdigest():
                    data.pop('key')
                    data['init'] = time()
                    data['exp'] = data['init'] + 86400
                    k = jwt.encode(data, '65aea63a16bf4e1ba415f0215cbfee55')
                    return {'token':k}
                return {'message': 'incorrect credentials'}
            return {"message":"UnAuthorized"}
        return {"message":"Not valid inputs"}