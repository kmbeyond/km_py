
from flask_restful import Resource, reqparse
import pymysql

from models.user import UserModel

class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    def __init__(self, _id, username, password):
        self.id=_id
        self.username =username
        self.password=password


    def post(self):
        data=UserRegister.parse.parse_args()

        if(UserModel.find_by_username(data['username']):
            return {"message": "A user already exists"}, 400

        #insert the user data
        conn = pymysql.connect(host="localhost",  # your host
                     user="km",       # username
                     passwd="km@1234",     # password
                     db="mycompany")   # name of the database

        # Create a Cursor object to execute queries.
        #cur = conn.cursor()

        #sql_sel_user="SELECT ID, USERNAME, '***' from T_USER where USERNAME=%s AND PASSWD=sha1(%s)"
        #rows = cur.execute(sql_sel_user, (username, password,))
        #row = cur.fetchone()
        #if rows == 0:
        #    user = None
        #else:
            #user = cls(row[0], row[1], "***")
        conn.close()
        return {"message": "User created successfully"}
