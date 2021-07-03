from flask import request
from flask_restful import Resource
from db import db

class Feed(Resource):
    def get(self):
        if request.args.get('key') and request.args.get('key').strip() == 'e75774559e4c4532a313769f7294d70b':
            k = db.fetch()
            z = {}
            for ind,a in  enumerate(k):
                z[ind] = a
            return z
        return {"message":"key missing"}
