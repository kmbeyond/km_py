from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.sqlite_operator import SqliteOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
from airflow.utils.dates import days_ago
import logging

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


default_args = {
    'owner': 'km',
}

with DAG(
        dag_id='dag_sqlite_ops',
        default_args=default_args,
        schedule_interval=None,
        start_date=days_ago(2),
        dagrun_timeout=timedelta(minutes=60),
        tags=['km'],
        params={"example_key": "example_value"},
        catchup=False
) as dag:
    bash_task1 = BashOperator(
        task_id='bash_task1',
        bash_command='echo "Executing as user: `echo $USER`";'
    )

    insert_record = SqliteOperator(
        task_id="insert_record",
        sqlite_conn_id="my_sqlite_conn",
        sql="INSERT INTO test_table(id,name) VALUES (?,?)",
        parameters=tuple([1,'Adam'])
    )

    #using Hook
    #@dag.task(task_id="insert_record")
    #def insert_sqlite_hook():
    #    sqlite_hook = SqliteHook(sqlite_conn_id="my_sqlite_conn")
    #    rows = [(1, 'Adam'), (4, 'Harry')]
    #    target_fields = ['id', 'name']
    #    sqlite_hook.insert_rows(table='test_table', rows=rows, target_fields=target_fields)

    db_query = SqliteOperator(
        task_id="db_query",
        sqlite_conn_id="my_sqlite_conn",
        sql="SELECT * FROM test_table"
    )
    insert_record >> db_query
    #insert_sqlite_hook() >> db_query

if __name__ == "__main__":
    dag.cli()
