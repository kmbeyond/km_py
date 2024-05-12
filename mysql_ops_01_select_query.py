#mysql-connector : python3 -m pip install mysql-connector-python
#MySQLdb : python3 -m pip install pymysql

#-----get database config from config script
import mysql_ops_config as mysqlconf

#---using mysql
import mysql.connector as mysql_connector
conn1 = mysql_connector.connect(
  host = mysqlconf.mysql_host,
  user = mysqlconf.mysql_user,
  passwd = mysqlconf.mysql_passwd,   #OR password=mysql_passwd,
  database = mysqlconf.mysql_db
)
print("Connected to: ", conn1.get_server_info())
cursor = conn1.cursor()

result = cursor.execute("SHOW DATABASES")
print(result)
for x in cursor.fetchall():
  print(x)


#using pymysql
import pymysql
conn2 = pymysql.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db)
cursor = conn2.cursor()


#Build the sql String
search_emp = "emp3"
sql = f"""SELECT * FROM T_EMP"""
#            where EMP_CODE = '{search_emp}'"""

cursor.execute(sql)
for row in cursor.fetchall() :
    print(row)
    print(" -> {}, {}, {}, {}".format(row[0], row[1], row[2], row[3]))


#SQL with list arguments
#sql = "SELECT * FROM T_EMP where EMP_CODE=?"   #sqlite3
sql = "SELECT * FROM T_EMP where EMP_CODE=%s"  #mysql.connector
cursor.execute(sql, search_emp )
#ERROR: mysql.connector.errors.ProgrammingError: Could not process parameters: str(emp3), it must be of type list, tuple or dict

for row in cursor.fetchall() :
    print("{}, {}, {}, {}".format(row[0], row[1], row[2], row[3]))

#get all columns as list
table_name = "T_EMP"
cursor.execute("describe %s" % table_name)
all_columns = [ row[0] for row in cursor.fetchall() ]

#execute multiple SQL statements - NOT WORKING
sql = "SELECT 1; SELECT 2;"
cursor.execute(sql, multi=True)
for x in cursor.fetchall():
  print(x)




cursor.close()
conn1.close()
conn2.close()
