import time

from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow.decorators import dag, task

default_args = {
    'owner' : 'km'
}


@dag(dag_id='passing_data_with_taskflow_01',
     description = 'Xcom using the TaskFlow API',
     default_args = default_args,
     start_date = days_ago(1),
     schedule_interval = '@once',
     tags = ['km'])
def passing_data_with_taskflow_api():

    @task
    def get_code():
        import random
        return {'code': random.randint(0, 1)}

    @task
    def get_status(get_code: dict):
        get_code['status'] = 'Success' if get_code['code']==1 else 'Failure'
        return get_code

    @task
    def display_result(get_code_status: dict):
        print(f"Return Code: {get_code_status}")


    result_code = get_code()
    result_status = get_status(result_code)
    display_result(result_status)


passing_data_with_taskflow_api()


