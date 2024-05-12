import mysql_ops_config as mysqlconf

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


#Employee record
#for timestamp
import datetime
import time
ts = time.time()
created_timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

emp1 = ('111', 111, 'first1', 'last1', 1, 1)
#emp1 = (created_timestamp, '111', 111, 'first1', 'last1', 1, 1)

emp2={
    #"CREATED": created_timestamp,
    "EMP_CODE": "555",
    "USER_ID": 555,
    "FIRST_NAME": "first5",
    "LAST_NAME": "last5",
    "DEPT_ID": 1,
    "ADDR_ID": 1
}

#Check if DEPT_ID exists
sql_dept_select = "SELECT * from T_DEPT where ID=%s"
cursor.execute(sql_dept_select, (emp2["DEPT_ID"],))
rows = cursor.fetchall()
if len(rows) >= 1:
    if len(rows) > 1:     print(f"ERROR: There should ONLY ONE DEPT with ID: {emp2['DEPT_ID']}")
    else: print(f"Dept exists: {rows[0][0]} - {rows[0][1]}")
else:
    print("Dept not found")


#insert record
sql_insert = """INSERT into T_EMP (EMP_CODE, USER_ID, FIRST_NAME , LAST_NAME, DEPT_ID, ADDR_ID) 
          VALUES (%s, %s, %s, %s, %s, %s) """
cursor.execute(sql_insert, emp1)
conn1.commit()


#transaction
cursor = conn1.cursor()
conn1.autocommit(False)
try:
    sql_insert = """INSERT into T_EMP (EMP_CODE, USER_ID, FIRST_NAME , LAST_NAME, DEPT_ID, ADDR_ID) 
          VALUES (%s, %s, %s, %s, %s, %s) """
    cursor.execute(sql_insert, emp1)
    conn1.commit()
except:
    conn1.rollback()


cursor.close()
conn1.close()
