# -*- coding: utf-8 -*-
"""
Created on Wed Nov  10 09:14:46 2017

@author: Kiran
"""
#Requirements:
#--install pymysql (MySQLdb for Python 2.x)
#

#Employee record
emp1=('emp3','user3','first3', 'last3', 1, 1)

emp2={
    "EMP_CODE": "emp6",
    "USER_ID": 6,
    "FIRST_NAME": "first6",
    "LAST_NAME": "last6",
    "DEPT_ID": 1,
    "ADDR_ID": 1
}
#import MySQLdb #This is for Python 2.x
import pymysql

conn = pymysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="Iamroo@9090",     # password
                     db="mycompany")   # name of the database

# Create a Cursor object to execute queries.
cur = conn.cursor()

#Check if DEPT_ID exists
sql_dept_select="SELECT ID from T_DEPT where ID=%s"
rows = cur.execute(sql_dept_select, (emp2["DEPT_ID"],))
if rows>=1:
    print("Dept exists")
else:
    print("Dept not found")

#Check if ADDR_ID exists
sql_addr_select="SELECT ID from T_ADDR where ID=%s"
rows = cur.execute(sql_addr_select, (emp2["ADDR_ID"],))
if rows>=1:
    print("Address exists")
else:
    print("Address not found")

#Now insert T_EMP record
#sql_insert ="INSERT INTO T_EMP (EMP_CODE, USER_ID, FIRST_NAME ,LAST_NAME, DEPT_ID, ADDR_ID) VALUES (%s,%d,%s,%s,%d,%d)"
#cur.execute(sql_insert, emp1)
conn.autocommit(False)
try:
    sql_insert = "insert into `{table}` ({columns}) values ({values});".format(table="T_EMP", columns=",".join(emp2.keys()), values=", ".join(["%s"] * len(emp2)))
    print("INSERT Q: {}".format(sql_insert))
    cur.execute(sql_insert, list(emp2.values()))
    cur.execute("commit")
    conn.commit()
except:
    conn.rollback()

print("record insert completed.")


# print the first and second columns
#for row in cur.fetchall() :
#    print("{} , {}, {}, {}".format(row[0], row[1], row[2], row[3]))

cur.close()
conn.close()
