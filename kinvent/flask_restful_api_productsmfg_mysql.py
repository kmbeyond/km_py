
#RESTful service
#Start the service: python flask_restful_api_productsmfg_mysql.py
#Test using an API test tool ( Ex: PostMan, SoapUI)
#

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required


#import from our security.py file
from security import authenticate, identity
#from user.py import UserRegister
from resources.ProductsMfg import ProductsMfg


app = Flask(__name__)
app.secret_key = 'kmkey'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(ProductsMfg, '/productsmfg') #http://127.0.0.1:5000/productsmfg
#api.add_resource(ProductsMfg, '/productsmfg/<string:name>') #http://127.0.0.1:5000/productsmfg/PRD-001

if __name__ == '__main__':
    app.run(port=5000, debug=True)
