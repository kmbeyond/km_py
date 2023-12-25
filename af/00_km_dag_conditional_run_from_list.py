from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator   #v2
from airflow.operators.python import BranchPythonOperator  #v2
from airflow.operators.python_operator import PythonOperator, ShortCircuitOperator
#v1#from airflow.operators.dummy_operator import DummyOperator    #v1
#from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
#v1#from airflow.operators.python_operator import BranchPythonOperator   #v1
from airflow.utils.dates import days_ago
import random, logging
from airflow.utils.db import provide_session

task_list = ['task_1', 'task_2', 'task_3','task_4','task_5']

args = {
    'owner': 'km',
}

def print_context(**kwargs):
  print(f"****** Task Id: {kwargs['ti'].task_id}")
  for k,v in kwargs.items():
    logging.info(f'{k} = {v}')

def decide_next_steps():
  import random
  next_tasks = random.sample(task_list, random.randint(0, len(task_list)))

  #to expand it
  #next_tasks = []
  #for task in task_list:
  #  if bool(random.choice([True, False])): next_tasks.append(task)
  #shuffle sequence
  #random.shuffle(next_tasks)
  next_tasks.sort()
  logging.info(f"Tasks selected: {next_tasks}")
  print(f"Tasks to run: {next_tasks}")
  return next_tasks

@provide_session
def delete_xcom(session=None, **kwargs):
    from datetime import timezone, date, datetime, timedelta
    from airflow.models import XCom
    today_date = date.today().strftime('%Y-%m-%d')
    for arg in kwargs.items(): logging.info(f" ---> {arg[0]} = {arg[1]}")
    dag_id = kwargs['dag']._dag_id
    # dag_id = kwargs['ti'].dag_id
    print(f"**** Delete XCom of DAG: {dag_id}")
    dt_n_days_ago = (datetime.now().replace(tzinfo=timezone.utc) - timedelta(days=1)).replace(tzinfo=timezone.utc)
    try:
        session.query(XCom).filter((XCom.dag_id == dag_id) & (XCom.execution_date <= dt_n_days_ago)).delete(synchronize_session=False)
    except Exception as err:
        details_error = f"EXCEPTION: during deleting xcomms for dag_id: {dag_id}; older than: {dt_n_days_ago}: ERROR: {err}"
        logging.info(details_error)
        raise ValueError(details_error)

with DAG(
    dag_id='00_km_dag_conditional_run_from_list',
    default_args=args,
    schedule_interval=None,
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
 task_1 = DummyOperator(
   task_id='task_1'
 )

 task_2 = DummyOperator(
   task_id='task_2'
 )

 task_3 = DummyOperator(
   task_id='task_3'
 )
 task_4 = DummyOperator(
   task_id='task_4'
 )
 task_5 = PythonOperator(
   task_id='task_5',
   python_callable=print_context,
   provide_context=True,
   op_kwargs={}
 )
 delete_xcom = PythonOperator(
     task_id="delete_xcom",
     python_callable=delete_xcom,
     trigger_rule='none_failed',
     provide_context=True,
 )
 span_next_tasks >> [task_1, task_2, task_3, task_4, task_5] >> delete_xcom

if __name__ == "__main__":
    dag.cli()
