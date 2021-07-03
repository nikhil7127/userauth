import os
from flask import Flask,request
from flask_restful import Api, Resource
from update import Update
from login import Login
from register import Register
from delete import Delete
from feed import Feed
from db import db  

application = Flask(__name__)
api = Api(application)

api.add_resource(Login, "/auth/login")
api.add_resource(Register, "/auth/register")
api.add_resource(Delete,"/auth/delete")
api.add_resource(Update,"/auth/update")
api.add_resource(Feed,"/feed")

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=int(os.environ.get("POST", 8080)))
    db.close()

