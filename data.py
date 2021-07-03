from flask_restful import Resource
from db import token_required

class Data(Resource):
    @token_required
    def get(self):
        return {"application":"get"}