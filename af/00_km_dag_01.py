from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator
from airflow.utils.dates import days_ago
import logging


# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def km_function(**kwargs):
    print(f"Py function: km_function")


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


args = {
    'owner': 'airflow',
    'on_failure_callback': 'dag_failure_notification',
    'on_success_callback': 'dag_success_notification'
}

with DAG(
        dag_id='00_km_dag_01',
        default_args=args,
        schedule_interval=None,
        start_date=days_ago(2),
        dagrun_timeout=timedelta(minutes=60),
        tags=['km'],
        params={"example_key": "example_value"},
        catchup=False
) as dag:
    bash_task1 = BashOperator(
        task_id='bash_task1',
        bash_command='echo "Executing..."; echo "Airflow version:"`airflow version`; echo "Python:"`python -V`; echo "python3:"`python3 -V`; python3 -m pip list; exit 0'
    )

    dummy_task1 = DummyOperator(
        task_id='dummy_task1'
    )

    py_task1 = PythonOperator(
        task_id='py_task1',
        python_callable=km_function
    )

    bash_task1 >> dummy_task1 >> py_task1

if __name__ == "__main__":
    dag.cli()