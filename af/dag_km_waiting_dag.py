from datetime import datetime
import time
import pendulum

from airflow import DAG
from airflow.exceptions import AirflowFailException
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
wait_seconds = 720 # minutes * 60

with DAG(
    dag_id="dag_km_waiting_dag",
    #start_date=pendulum.today('UTC').add(days=-1),
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["km", "project"],
) as dag:

    start = EmptyOperator(task_id="start")

    wait_task = PythonOperator(
        task_id='wait',
        python_callable=lambda seconds=wait_seconds: time.sleep(seconds),
        op_kwargs={'seconds': wait_seconds}
    )

    end = EmptyOperator(task_id="end")

    start >> wait_task >> end


