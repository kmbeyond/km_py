from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator
from airflow.utils.dates import days_ago


def km_function(**kwargs):
    print(f"Py function: km_function")


def dag_failure_notification(**kwargs):
    print("DAG Failed")


def dag_success_notification(**kwargs):
    print("DAG Success")


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
        bash_command='echo "Executing..."; echo "Airflow version:"`airflow version`; echo "Python:"`python -V`; echo "python3:"`python3 -V`; exit 0'
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