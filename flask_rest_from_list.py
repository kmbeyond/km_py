#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:28:01 2017

@author: kiran
"""

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

#We will create list of stores (each store has a name & store items ) as JSON
stores = [
        {
                'name': 'store1',
                'items': [
                        { 'name': 'item1.1',
                         'price': 16.99
                         }
                        
                ]
        }
    ]

@app.route("/")
#Sample request: http://127.0.0.1:5000/
def home():
    return render_template('index.html')

#GET - used to send data back (default)
#POST - used to receive data

#Add a store (without items)
#POST /store data:{name:} --WORKING
@app.route('/store', methods=['POST'])
#Sample request: http://127.0.0.1:5000/store
#Method=  POST
#Body= {  "name": "store2" }
def create_store():
    request_data=request.get_json()
    new_store={ 'name': request_data['name'],
               'items':[]
               }
    stores.append(new_store)
    return jsonify(new_store)

#Get specific store
#GET /store/<string:name> --WORKING
#Sample request: http://127.0.0.1:5000/store/store1
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

#Get all stores (with items)
#GET /store --WORKING
#Sample req: http://127.0.0.1:5000/store  - GET
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

#Add item to store
#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
#Sample req: http://127.0.0.1:5000/store/store2/item
#Body: {
#  "name": "item2.1",
#  "price": 22.11
#}
def create_item_in_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                    'name': request_data['name'],
                    'price': request_data['price']
                    }
            store['items'].append(new_item)
            return jsonify(stores)
    return jsonify({'message': 'store {} is not found /store/<string:name>/item'.format(name)})

#Get items of a store
#GET /store/<string:name>/item --WORKING
@app.route('/store/<string:name>/item')
#Sample req: http://127.0.0.1:5000/store/store2/item
def get_items_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

#Delete specific store
#DELETE /store/<string:name> --WORKING
@app.route('/store/<string:storeName>', methods=['DELETE'])
#Sample req: http://127.0.0.1:5000/store/store2
def delete_store(storeName):
    for store in stores:
        if store['name']==storeName:
           stores.remove(store)
           return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

#Delete item from a store
#DELETE /store/<string:name>/item/<itemname> --NOT WORKING
@app.route('/store/<string:storeName>/item/<string:itemName>', methods=['DELETE'])
#Sample req: http://127.0.0.1:5000/store/store2/item
def delete_items_in_store(storeName, itemName):
    for store in stores:
        if store['name']==storeName:
            for item in store['items']:
                if item['name']==itemName:
                    stores[0].items()
            return jsonify({'items': store['items']})
    return jsonify({'message': 'item not found'})


app.run(port=5000)
