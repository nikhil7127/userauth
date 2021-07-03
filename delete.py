from flask import request
from flask_restful import Resource
from db import db

class Delete(Resource):
    def get(self):
        if request.args.get('key') and request.args.get('email'):
            if request.args.get('key') == 'e75774559e4c4532a313769f7294d70b':
                return db.delete(request.args.get('email').strip())
        return {'error':'UnAuthorized'}