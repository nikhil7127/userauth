from flask import request
from flask_restful import Resource
from db import db
from hashlib import sha256

class Register(Resource):
    def get(self):
        data = request.args.to_dict()
        if data.get('username') and data.get('password') and data.get('email') and data.get('key'):
            if data['key'] == 'e75774559e4c4532a313769f7294d70b':
                k = db.add((data['username'].strip(),data['email'].strip(),sha256(data['password'].strip().encode()).hexdigest()))
                return {"message":str(k)}
            return {"message":"UnAuthorized"}
        return {"message":"Not valid inputs"}