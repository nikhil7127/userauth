import os
from flask import Flask,request
from flask_restful import Api, Resource
from models import Database
from hashlib import sha256

################################################################

application = Flask(__name__)
api = Api(application)
db = Database()

################################################################


class Register(Resource):
    def get(self):
        data = request.args.to_dict()
        if data.get('username') and data.get('password') and data.get('email') and data.get('key'):
            if data['key'] == 'e75774559e4c4532a313769f7294d70b':
                k = db.add((data['username'].strip(),data['email'].strip(),sha256(data['password'].strip().encode()).hexdigest()))
                return {"message":str(k)}
            return {"message":"UnAuthorized"}
        return {"message":"Not valid inputs"}

################################################################


class Login(Resource):
    def get(self):
        data = request.args.to_dict()
        if data.get('password') and data.get('email') and data.get('key'):
            if data['key'] == 'e75774559e4c4532a313769f7294d70b':
                user = db.findUser(data['email'].strip())[0]
                if user == sha256(data['password'].strip().encode().hexdigest()):
                    return {'status': 'done'}
                return {'message': 'incorrect credentials'}
            return {"message":"UnAuthorized"}
        return {"message":"Not valid inputs"}

################################################################


class Show(Resource):
    def get(self):
        if request.args.get('key') == 'e75774559e4c4532a313769f':
            k = db.fetch()
            z = {}
            for ind,a in  enumerate(k):
                z[ind] = a
            return z
        return {"message":"error"}

api.add_resource(Login, "/auth/login")
api.add_resource(Register, "/auth/register")
api.add_resource(Show,"/feed")


if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=int(os.environ.get("POST", 8080)))

    db.close()

