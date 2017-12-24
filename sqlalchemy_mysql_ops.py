

from sqlalchemy import create_engine

#THIS MAY GIVE ERROR FOR NEW VERSIONS OF MySQL
engine = create_engine("{}://{}:{}@{}:{}/{}".format("mysql+pymysql", "km", "'Kiran$5july@123'", "", "3306", "kmdb") )

engine = create_engine("{}://{}:{}@{}:{}/{}?charset=utf8mb4".format("mysql+pymysql", "km", "'Kiran$5july@123'", "", "3306", "kmdb") )

#OR/Same as:  engine = create_engine("mysql+pymysql://km:'Kiran$5july@123'@/kmdb?charset=utf8mb4")

connection = engine.connect()
connection = connection.execution_options(
    isolation_level="READ COMMITTED"
)
'''
Valid values for isolation_level include:

    READ COMMITTED
    READ UNCOMMITTED
    REPEATABLE READ
    SERIALIZABLE
    AUTOCOMMIT
'''
#2 methods of connections
#1: create an explicit connection & must close connection
result = connection.execute("select name from kmdb.EMP")
for row in result:
    print("Emp Name: ", row['name'])
connection.close()

#2: execute directly using engine, uses connection from pool & closes automatically after use
result = engine.execute("select name from kmdb.EMP")
for row in result:
    print("Emp Name: ", row['name'])
result.close()


#-------------commit-------------

conn = engine.connect()
conn.execute("INSERT INTO users VALUES (1, 'john')")  # autocommits

#explicit autocommit
engine.execute(text("SELECT my_mutating_procedure()").execution_options(autocommit=True))



#-------------transactions-----------
connection = engine.connect()
trans = connection.begin()
try:
    table1 = Table('users', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String(50))
    )
    r1 = connection.execute(table1.select())
    connection.execute(table1.insert(), col1=7, col2='this is some data')
    trans.commit()
except:
    trans.rollback()
    raise
