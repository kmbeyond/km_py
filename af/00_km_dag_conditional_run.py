from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.dates import days_ago
import random

args = {
    'owner': 'airflow',
}

def decide_next_step():
    return "task_zero" if random.randint(0,1)==0 else "task_one"

with DAG(
    dag_id='00_km_dag_conditional_run',
    default_args=args,
    schedule_interval='* * * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['km'],
    params={"example_key": "example_value"},
    catchup=False
) as dag:

 is_zero_or_one = BranchPythonOperator(
   task_id="is_zero_or_one",
   #python_callable=lambda: "task_zero" if random.randint(0,1)==0 else "task_one"
   python_callable=decide_next_step
 )
 task_one = DummyOperator(
   task_id='task_one'
 )

 task_zero = DummyOperator(
   task_id='task_zero'
 )

 is_zero_or_one >> [task_one, task_zero]

if __name__ == "__main__":
    dag.cli()