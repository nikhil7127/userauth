from flask import request
from flask_restful import Resource
from db import db

class Update(Resource):
    def get(self):
        if request.args.get('key') and request.args.get('email') and request.args.get('username'):
            if request.args.get('key') == 'e75774559e4c4532a313769f7294d70b':
                return db.update(request.args.get('email').strip(),request.args.get('username').strip())
        return {'error':'UnAuthorized'}