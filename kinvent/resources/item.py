from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

#We use this as store instead of models.ItemModel
items = []

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    #@jwt_required()
    def get(self, name):
        #We will replace these lines using filter()
        #for item in items:
        #    if item['name'] == name:
        #        return item
        #return {'item': None}, 404
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    #@jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'An item with name {} already exists'.format(name)}, 400

        #data = request.get_json()
        data=Item.parser.parse_args()

        item={'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    #@jwt_required()
    def delete(self, name):
        global items
        items=list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item: {} deleted'.format(name)}

    #@jwt_required()
    def put(self, name):

        #data = request.get_json()
        data=Item.parser.parse_args()

        item =next(filter(lambda x: x['name'] == name, items), None)
        if item:
            item.update(data)
        else:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        return item

class ItemList(Resource):
    #@jwt_required()
    def get(self):
        return {'items': items}
