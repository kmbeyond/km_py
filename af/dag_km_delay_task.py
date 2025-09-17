
from datetime import datetime, timedelta
import logging, airflow, yaml
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

#import pendulum
from airflow.sensors.time_delta import TimeDeltaSensor
from airflow.sensors.time_delta import TimeDeltaSensorAsync
from airflow.sensors.python import PythonSensor

# logging setup
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def view_objects(*args, **kwargs):
    logging.info(f"Objects: {dir(airflow.sensors)}")
    return True

def dag_success_notification(context, **kwargs):
    logger.info("DAG Success")
    #print_context(context)

def dag_failure_notification(context, **kwargs):
    logger.info("DAG Failed")
    logger.error("DAG Failed")
    #print_context(context)

def print_context(context):
    for k,v in context.items():
        logging.info(f"{k} -> {v}")


default_args = {
    'owner': 'km',
    'retries': 0,
    'start_date': airflow.utils.dates.days_ago(2),
    'retry_delay': timedelta(seconds=0),
    'on_failure_callback': dag_failure_notification,
    'on_success_callback': dag_success_notification
}

with DAG('dag_km_delay_task', default_args=default_args, schedule_interval=None, catchup=False, tags=['km']) as dag:

    #dummy_task1 = DummyOperator(task_id='dummy_task1')
    bash_task1 = BashOperator(
        task_id="bash_task1",
        bash_command='pwd; ls -lt /usr/local/airflow/;'
    )

    #delay_task = TimeDeltaSensor(   #pokes periodically
    #    task_id="delay_task",
    #    delta=timedelta(minutes=2),  #pendulum.duration(minutes=5),
    #    mode = 'reschedule'    #releases worker between pokes
    #)

    delay_task2 = TimeDeltaSensorAsync(  #defers to triggerer
        task_id="delay_task2",
        delta=timedelta(seconds=60),   #pendulum.duration(minutes=10),
        mode='reschedule'
    )
  
    #python function is called, function should return True within timeout else fails
    #delay_task_py = PythonSensor(
    #    task_id="delay_task_py",
    #    timeout=120,  #timeout in seconds
    #    poke_interval=300,    #poke in every seconds
    #    #soft_fail=False,   #default is Fail
    #    python_callable = view_objects,
    #    mode='reschedule'
    #)

    bash_task2 = BashOperator(
        task_id="bash_task2",
        bash_command='pwd'
    )

    bash_task1 >> delay_task2 >> bash_task2
    #bash_task1 >> delay_task2 >> delay_task_py >> bash_task2
