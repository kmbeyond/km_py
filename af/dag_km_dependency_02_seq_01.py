from datetime import datetime, timedelta
import logging, airflow, yaml
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.external_task import ExternalTaskMarker


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



def py_start_task(to_email_address, *args, **kwargs):
    logging.info(f"Email to {to_email_address}")


default_args = {
    'owner': 'airflow',
    'retries': 3,
    'start_date': airflow.utils.dates.days_ago(2),
    'retry_delay': timedelta(seconds=10),
    'on_failure_callback': dag_failure_notification,
    'on_success_callback': dag_success_notification
}
#    'start_date': datetime.datetime(2021, 09, 01) #airflow.utils.dates.days_ago(2),


with DAG('dag_km_dependency_02_seq_01', default_args=default_args, tags=['km'], schedule_interval='* * * * *', catchup=False, dagrun_timeout=timedelta(minutes=90)) as dag:
    py_start_task = PythonOperator(
        task_id='py_start_task',
        python_callable=py_start_task,
        provide_context=True,
        op_kwargs={
            'to_email_address': to_email_address,
        }
    )
    py_start_task

    #notify_downstream_task = ExternalTaskMarker(
    #    task_id="notify_downstream_task",
    #    external_dag_id="dag_km_dependency_02_seq_02",
    #    external_task_id="downstream_task",
    #)
    #notify_downstream_task
