from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.ProductsMfg import ProductsMfgModel


class ProductsMfg(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('product_cd',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('qty',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('mfg_dt',
        type=str,
        required=False
    )
    parser.add_argument('mfg_unit_cd',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('machine_cd',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('warehouse_cd',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    #@jwt_required()
    def post(self):
        #data = request.get_json()
        data = ProductsMfg.parser.parse_args()

        record={ "product_cd": data["product_cd"],
                "qty": data["qty"],
                "mfg_dt": data["mfg_dt"],
                "mfg_unit_cd": data["mfg_unit_cd"],
                "machine_cd": data["machine_cd"],
                "warehouse_cd": data["warehouse_cd"] }

        #if record['product_cd'] == null:
            #return {'message': 'product_cd is blank'.format(name)}, 400
        resp = ProductsMfgModel.addToInventory(record)
        if resp['Success'] == "Y":
            return resp, 201
        else:
            return {"Error": resp['Success']}, 500
