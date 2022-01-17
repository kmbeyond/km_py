from datetime import datetime, timedelta
import logging
import airflow.hooks.S3_hook
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
#from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

# from airflow.operators.email_operator import EmailOperator

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# snowflake connection
# snowflake_hook = SnowflakeHook(snowflake_conn_id=config['snowflake_conn_id'], autocommit=False)
# snowflake_hook_autocommit = SnowflakeHook(snowflake_conn_id=config['snowflake_conn_id'])
# cs = snowflake_hook.get_cursor()
# cs_autocommit = snowflake_hook_autocommit.get_cursor()


def email_status():
    import airflow
    airflow.utils.email.send_email('km@gmail.com', 'TEST SUBJECT', '<h3>email test</h3>')


def my_args(*args, **kwargs):
    print("My Args are {}".format(args))
    print("My Kwargs are {}".format(kwargs))


def dag_failed_notification(**kwargs):
    print("DAG Failed")

def dag_success_notification(**kwargs):
    print("DAG Success")

default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
    'retries': 3,
    'retry_delay': timedelta(minutes=0),
    'on_failure_callback': 'dag_failed_notification',
    'on_success_callback': 'dag_success_notification'
}

with DAG('dag_km_test', default_args=default_args, schedule_interval='0 12 1 * *', catchup=False,
         dagrun_timeout=timedelta(minutes=90)) as dag:
    dummy_task = DummyOperator(task_id='dummy_task')
    #dummy_task

    bash_task = BashOperator(
        task_id='bash_task',
        bash_command="""echo 'Welcome Bash'"""
    )
    dummy_task >> bash_task

    email_task = PythonOperator(
        task_id='email_task',
        python_callable=email_status
    )
    dummy_task >> email_task

    # email_task = EmailOperator(
    #    task_id='email_task',
    #    to='km@gmail.com',
    #    subject='Airflow Alert',
    #   html_content=""" <h3>Email Test</h3> """,
    # )
    # dummy_task >> email_task

    py_args_test = PythonOperator(
        task_id='py_args_test',
        python_callable=my_args,
        op_args={'a', 'b', 'c'},
        op_kwargs={'a': '2'},
    )
    dummy_task >> py_args_test