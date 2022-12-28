import logging, airflow
#from airflow.operators.python_operator import PythonOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import timedelta, datetime, timezone
from airflow.models import XCom
from airflow.utils.db import provide_session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.getLogger('botocore').setLevel(logging.CRITICAL)

# DAG config
dags_to_delete_xcomms = ['km_xcom_ops']
n_days_ago = 10
dt_today = datetime.now().replace(tzinfo=timezone.utc)
dt_n_days_ago = (dt_today - timedelta(days=n_days_ago)).replace(tzinfo=timezone.utc)

def create_xcom(**kwargs):
    ti = kwargs['ti']
    ti.xcom_push(key='my_key1', value=dt_today.strftime( '%Y-%m-%d %H:%M:%S' ) )

@provide_session
def delete_xcom(session=None, **kwargs):
    #dag_id = kwargs['dag']._dag_id
    for dag_id in dags_to_delete_xcomms:
        logging.info(f"Deleting XComm for dag_id: {dag_id}; older than: {dt_n_days_ago}")
        try:
            session.query(XCom).filter((XCom.dag_id == dag_id) & (XCom.execution_date <= dt_n_days_ago) ).delete()
        except Exception as err:
            details_error = f"EXCEPTION: during deleting xcomms for dag_id: {dag_id}; older than: {dt_n_days_ago}"
            logging.info(details_error)
            #utils_email.email_api_publish_message("ppa_delete_xcomm", "delete_xcom", "EXCEPTION", details_error)


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

with DAG('dag_create_xcom', default_args=default_args, schedule_interval='0 12 * * *', catchup=False, tags=['km']) as dag:
    create_xcom = PythonOperator(
        task_id="create_xcom",
        python_callable=create_xcom
    )
    create_xcom

    delete_xcom = PythonOperator(
        task_id="delete_xcom",
        python_callable = delete_xcom
    )

    delete_xcom
