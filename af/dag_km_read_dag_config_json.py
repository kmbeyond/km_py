from datetime import timedelta
from airflow.providers.standard.operators.python import BranchPythonOperator, PythonOperator
from airflow.sdk import DAG
import pendulum
from airflow.sdk import task, dag, get_current_context


# logging setup
import logging
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)

def f_read_config_json(**context):
    print(f"Py function: f_read_config_json")
    conf = context['dag_run'].conf
    logging.info(f"conf: {conf}")
    logging.info(f"start_date: {conf.get('start_date')}")
    conf_dag_key = [k for k in conf.keys() if "dag" in k]
    logging.info(f"conf_keys: {conf_dag_key}")


args = {
    'owner': 'airflow',
}

with DAG(
        dag_id='dag_km_read_dag_config_json',
        default_args=args,
        schedule=None,
        start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
        dagrun_timeout=timedelta(minutes=60),
        tags=['km'],
) as dag:

    read_config_json = PythonOperator(
        task_id='read_config_json',
        python_callable=f_read_config_json
    )

    read_config_json

#if __name__ == "__main__":
#    dag.cli()
