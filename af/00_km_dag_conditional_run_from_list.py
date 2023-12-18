from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.dates import days_ago
import random, logging

task_list = ['task_one', 'task_two', 'task_three','task_four','task_five']

args = {
    'owner': 'km',
}

def decide_next_steps():
  import random
  next_tasks = []
  for task in task_list:
    if bool(random.choice([True, False])): next_tasks.append(task)

  #if want to shuffle sequence
  random.shuffle(next_tasks)
  logging.info(f"Tasks selected: {next_tasks}")
  print(f"Tasks to run: {next_tasks}")
  return next_tasks

with DAG(
    dag_id='00_km_dag_conditional_run_from_list',
    default_args=args,
    schedule_interval='* * * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['km'],
    params={"example_key": "example_value"},
    catchup=False
) as dag:

 span_next_tasks = BranchPythonOperator(
   task_id="span_next_tasks",
   python_callable=decide_next_steps
 )
 task_one = DummyOperator(
   task_id='task_one'
 )

 task_two = DummyOperator(
   task_id='task_two'
 )

 task_three = DummyOperator(
   task_id='task_three'
 )
 task_four = DummyOperator(
   task_id='task_four'
 )
 task_five = DummyOperator(
   task_id='task_five'
 )
 span_next_tasks >> [task_one, task_two, task_three, task_four, task_five]

if __name__ == "__main__":
    dag.cli()
