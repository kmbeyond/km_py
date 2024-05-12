
#-----get database config
import os

mysql_host = os.environ.get('MYSQL_HOST')
#mysql_host = os.getenv('MYSQL_HOST')
mysql_port = os.environ.get('MYSQL_PORT')
mysql_db = os.environ.get('MYSQL_DB')
mysql_user = os.environ.get('MYSQL_USER')
mysql_passwd = os.environ.get("MYSQL_PWD")

