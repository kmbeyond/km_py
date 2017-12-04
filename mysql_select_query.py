# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:42:46 2017

@author: SZTJC5
"""
#Requirements:
#--install MySQLdb
#

#import MySQLdb #This is for Python 2.x
import pymysql

conn = pymysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="Iamroo@9090",     # password
                     db="mycompany")   # name of the database

# Create a Cursor object to execute queries.
cur = conn.cursor()

#Build the sql String
#SQL as plain String
sql_select = "SELECT T_EMP.* FROM T_EMP " \
    " where EMP_CODE = '{}'".format("emp3")
# Execute the SQL
rows = cur.execute(sql_select)
print("Rows: {}".format(rows))
for row in cur.fetchall() :
    print("{}, {}, {}, {}".format(row[0], row[1], row[2], row[3]))


#SQL with list arguments
sql_select = "SELECT * FROM T_EMP where ID>%s"
# Execute the SQL
rows = cur.execute(sql_select, [0])
print("Rows: {}".format(rows))
for row in cur.fetchall() :
    print("{}, {}, {}, {}".format(row[0], row[1], row[2], row[3]))



'''
print("Query directly into row:")
sql_select = "SELECT * FROM T_EMP"
cur.execute(sql_select)
for row in cur:
    print("{}, {}, {}, {}".format(row[0], row[1], row[2], row[3]))
    #print(row)

########User Query
username="km"
password = "km@1234"

#Check user
sql_sel_user="SELECT ID, USERNAME from T_USER where USERNAME=%s AND PASSWD=sha1(%s)"
rows = cur.execute(sql_sel_user, (username, password,))
row = cur.fetchone()
if rows == 0:
    print("User NOT found")
else:
    print("User {} found".format(username))
##################
'''

cur.close()
conn.close()
