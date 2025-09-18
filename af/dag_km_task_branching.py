
from datetime import datetime, timedelta
import logging, airflow, yaml
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator, PythonOperator
import random
from airflow.utils.trigger_rule import TriggerRule

# logging setup
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def decide_next(**kwargs):
    random_number = random.randint(0,1)
    logging.info(f"Random Number: {random_number}")
    return "c" if random_number==0 else "d"

default_args = {
    'owner': 'km',
    'retries': 0,
    'start_date': airflow.utils.dates.days_ago(2),
    'retry_delay': timedelta(seconds=0)
}

with DAG('dag_km_task_branching', default_args=default_args, schedule_interval=None, catchup=False, tags=['km']) as dag:

    a = DummyOperator(task_id='a')
    b = BranchPythonOperator(
            task_id="b",
            python_callable=decide_next,
            op_kwargs={},
            provide_context=True,
    )
    c = BashOperator(
        task_id="c",
        bash_command='pwd; ls -lt /usr/local/airflow/;'
    )

    d = BashOperator(
        task_id="d",
        bash_command='pwd',
        #trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS
        trigger_rule = TriggerRule.ONE_SUCCESS
    )

    a >> b
    b >> c >> d
    b >> d
