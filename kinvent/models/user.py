

import pymysql

class UserModel:
    def __init__(self, _id, username, password):
        self.id=_id
        self.username =username
        self.password=password

    @classmethod
    def find_by_username(cls, username, password):

        conn = pymysql.connect(host="localhost",  # your host
                     user="km",       # username
                     passwd="Kiran$5july@123",     # password
                     db="mycompany")   # name of the database

        # Create a Cursor object to execute queries.
        cur = conn.cursor()

        #Check user
        sql_sel_user="SELECT ID, USERNAME, '***' from T_USER where USERNAME=%s AND PASSWD=sha1(%s)"
        rows = cur.execute(sql_sel_user, (username, password,))
        row = cur.fetchone()
        if rows == 0:
            user = None
        else:
            #user = cls(row[0], row[1], "***")
            user = cls(*row)

        conn.close()
        return user

    @classmethod
    def find_by_userid(cls, _id):

        conn = pymysql.connect(host="localhost",  # your host
                     user="km",       # username
                     passwd="Kiran$5july@123",     # password
                     db="mycompany")   # name of the database

        # Create a Cursor object to execute queries.
        cur = conn.cursor()

        #Check user
        sql_sel_user="SELECT ID, USERNAME '***' from T_USER where ID=?"
        rows = cur.execute(sql_sel_user, (_id,))
        row = cur.fetchone()
        if rows == 0:
            user = None
        else:
            #user = cls(row[0], row[1], "***")
            user = cls(*row)

        conn.close()
        return user
