from datetime import datetime, timedelta
import logging, json, boto3, airflow, requests
import airflow.hooks.S3_hook
from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.operators.python_operator import PythonOperator
#from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
#from base64 import urlsafe_b64encode as km64e, urlsafe_b64decode as km64d

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

to_email_address = "km@gmail.com"

def dag_success_notification(context, **kwargs):
    logger.info("DAG Success")
    print_context(context)


def dag_failure_notification(context, **kwargs):
    logger.info("DAG Failed")
    logger.error("DAG Failed")
    print_context(context)


def print_context(context):
    for k,v in context.items():
        logging.info(f"{k} -> {v}")


def send_af_email(to_email_address):
    import airflow
    airflow.utils.email.send_email(to_email_address, 'TEST af util email', '<h3>email test</h3>')

default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
    'on_failure_callback': dag_failure_notification,
    'on_success_callback': dag_success_notification
}

with DAG('dag_km_email', default_args=default_args, schedule_interval=None, catchup=False, dagrun_timeout=timedelta(minutes=90)) as dag:

    dummy_task = DummyOperator(task_id='dummy_task')

    email_task_emailop = EmailOperator(
        task_id='email_task_emailop',
        to=to_email_address,
        subject='Airflow Alert',
       html_content=""" <h3>Email Test</h3> """,
    )
    dummy_task >> email_task_emailop

    send_af_email = PythonOperator(
        task_id='send_af_email',
        python_callable=send_af_email,
        provide_context=True,
        op_kwargs={
            'to_email_address': to_email_address,
        }
    )
    dummy_task >> send_af_email
