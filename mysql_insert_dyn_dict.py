
#This takes all columns of the table to build the SQL
#Builds column values from Dictionary

#import MySQLdb #This is for Python 2.x
import pymysql


def add_row(cursor, tablename, rowdict):
    # XXX tablename not sanitized
    # XXX test for allowed keys is case-sensitive

    # filter out keys that are not column names
    cursor.execute("describe %s" % tablename)
    all_keys = set(row[0] for row in cursor.fetchall())
    keys = all_keys.intersection(rowdict)

    if len(rowdict) > len(keys):
        unknown_keys = set(rowdict) - allowed_keys
        print >> sys.stderr, "skipping keys:", ", ".join(unknown_keys)


    columns = ", ".join(keys)
    print("Columns: {}".format(columns))
    values_template = ", ".join(["%s"] * len(keys))
    print("Values_template: {}".format(values_template))

    sql = "insert into %s (%s) values (%s)" % (
            tablename, columns, values_template)
    print("SQL: {}".format(sql))

    values = tuple(rowdict[key] for key in keys)
    print("values: {}".format(values))
    cursor.execute(sql, values)
    print("Record inserted: {}".format(cursor.lastrowid))

emp2={
    "EMP_CODE": "emp6",
    "USER_ID": 6,
    "FIRST_NAME": "first6",
    "LAST_NAME": "last6",
    "DEPT_ID": 1,
    "ADDR_ID": 1
}


conn = pymysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="Iamroo@9090",     # password
                     db="mycompany")   # name of the database

cursor = conn.cursor()
#with open(filename) as instream:
#    row = json.load(instream)
#    add_row(cursor, "T_EMP", row)

add_row(cursor, "T_EMP", emp2)
conn.commit()
