import time
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.decorators import dag, task

default_args = {
    'owner':'km'
}

@dag(dag_id='dag_with_taskflow',
     description = 'DAG using Taskflow API',
     start_date = days_ago(1),
     default_args = default_args,
     schedule_interval = '@once',
     tags = ['km']
     )
def dag_with_taskflow_api():
    @task
    def task_1():
        print('***** Executing: Task1')

    @task
    def subtask_1():
        print('***** Executing: SubTask1')

    @task
    def subtask_2():
        print('***** Executing: SubTask2')

    @task
    def ending_task():
        print('***** Executing: ending_task')

    task_1() >> [subtask_1(), subtask_2()] >> ending_task()

dag_with_taskflow_api()
