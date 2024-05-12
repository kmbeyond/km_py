
#Function to dynamically build SQL statement from dictionary/json & insert
#get all keys from dictionary, sort & build SQL

#import MySQLdb #This is for Python 2.x
import pymysql


#-----get database config from config script
import mysql_ops_config as mysqlconf

#using pymysql
import pymysql
conn2 = pymysql.connect(host = mysqlconf.mysql_host,
                        user = mysqlconf.mysql_user, passwd = mysqlconf.mysql_passwd,
                        db = mysqlconf.mysql_db)
cursor = conn2.cursor()


def add_row(cursor, tablename, row_dict):
    # get all columns
    cursor.execute("describe %s" % tablename)
    all_columns = set(row[0] for row in cursor.fetchall())
    keys_to_insert = all_columns.intersection(row_dict)
    keys_omitted = all_columns.difference(row_dict)

    if len(keys_omitted) >= 1:
        print(f"skipping keys: {', '.join(keys_omitted)}")

    sorted_row_dict = dict(sorted(row_dict.items()))

    cols_to_insert = ", ".join(keys_to_insert)
    print("Columns to insert: {}".format(cols_to_insert))

    values_template = ", ".join(["%s"] * len(keys_to_insert))
    print("Values_template: {}".format(values_template))

    sql = f"""insert into {tablename} ({cols_to_insert}) 
               values ({values_template})"""
    print(f"SQL: {sql}")

    values = tuple(row_dict[key] for key in keys_to_insert)
    print("values: {}".format(values))

    cursor.execute(sql, values)
    print("Record inserted: {}".format(cursor.lastrowid))

#with open(filename) as instream:
#    row = json.load(instream)
#    add_row(cursor, "T_EMP", row)

tablename = "T_EMP"
emp2={
    "EMP_CODE": "emp5",
    "USER_ID": 5,
    "FIRST_NAME": "first5",
    "LAST_NAME": "last5",
    "DEPT_ID": 1,
    "ADDR_ID": 1
}
add_row(cursor, "T_EMP", emp2)
conn2.commit()



