from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

#import from our security.py file
from security import authenticate, identity
from resources.item import Item, ItemList


app = Flask(__name__)
app.secret_key = 'kmkey'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

#All Item & ItemList are moved to the resources, models packages

api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/item/Piano
api.add_resource(ItemList, '/items')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
