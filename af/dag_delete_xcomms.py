import logging, airflow
from airflow.operators.python_operator import PythonOperator
from airflow import DAG
from datetime import timedelta, datetime, timezone
from airflow.models import XCom
from airflow.utils.db import provide_session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.getLogger('botocore').setLevel(logging.CRITICAL)

# DAG config
dags_to_delete_xcomms = ['km_dag1']
n_days_ago = 30
dt_today = datetime.now().replace(tzinfo=timezone.utc)
dt_n_days_ago = (dt_today - timedelta(days=n_days_ago)).replace(tzinfo=timezone.utc)

@provide_session
def delete_xcom(session=None, **kwargs):
    #dag_id = kwargs['dag']._dag_id
    for dag_id in dags_to_delete_xcomms:
        logging.info(f"Deleting XComm for dag_id: {dag_id}; older than: {dt_n_days_ago}")
        try:
            session.query(XCom).filter((XCom.dag_id == dag_id) & (XCom.execution_date <= dt_n_days_ago) ).delete(synchronize_session='fetch')
        except Exception as err:
            details_error = f"EXCEPTION: during deleting xcomms for dag_id: {dag_id}; older than: {dt_n_days_ago}\n** ERROR: {err}"
            logging.info(details_error)
            raise ValueError(details_error)


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



default_args = {
    "owner": "km",
    "start_date": airflow.utils.dates.days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=0),
    'provide_context': True,
    'on_failure_callback': dag_failure_notification,
    'on_success_callback': dag_success_notification
}

with DAG('km_delete_xcomm', default_args=default_args, schedule_interval='0 12 * * *', catchup=False, tags=['km']) as dag:

    delete_xcom = PythonOperator(
        task_id="delete_xcom",
        python_callable = delete_xcom
    )

    delete_xcom
