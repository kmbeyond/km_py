import os,logging, subprocess
import airflow
import datetime, yaml
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
#from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('airflow.task')


def run_dbt_model_py(**kwargs):
    env = os.environ.copy()
    bash_command=f'''
            source $AIRFLOW_HOME/dbt_venv/bin/activate &&
            cd /usr/local/airflow/dbt/km_test_sf/ &&
            #dbt deps &&
            echo '[INFO] Starting dbt model: km_trust_src_tbl1' &&
            dbt run --select km_trust_src_tbl1 &&
            status=$? &&
            date &&
            echo "[INFO] Finished dbt model: km_trust_src_tbl1 with status $status" &&
            exit $status
    '''
    process = subprocess.Popen(bash_command, shell=True, env=env, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)



args = {
    'owner': 'km',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    "start_date": datetime(2023, 2, 7),
}

query_params = {}

with DAG('dag_km_run_dbt',
     max_active_runs=1,
     schedule_interval= None,
     default_args=args,
     tags=['km'],
     catchup=False
     ) as dag:


    run_dbt_model = BashOperator(
        task_id='run_dbt_model',
        bash_command=f'''source $AIRFLOW_HOME/dbt_venv/bin/activate &&
             #dbt --version &&
             cd /usr/local/airflow/dbt/km_test_sf/ &&
             dbt deps &&
             echo '[INFO] Starting dbt model: km_trust_src_tbl1';
             dbt run --select km_trust_src_tbl1;
             status=$?;
             echo "[INFO] Finished dbt model: km_trust_src_tbl1 with status $status";
             exit $status''',
    )

    run_dbt_model_py = PythonOperator(
        task_id='run_dbt_model_py',
        python_callable=run_dbt_model_py,
        provide_context=True,
        op_kwargs=query_params
    )

run_dbt_model >> run_dbt_model_py
