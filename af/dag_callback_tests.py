from datetime import timedelta

from airflow.sdk import DAG
#from airflow import DAG
from airflow.providers.standard.operators.python import BranchPythonOperator, PythonOperator
import logging, pendulum
from airflow.sdk import task, dag, get_current_context

import airflow_client.client
from airflow_client.client.api.dag_run_api import DagRunApi
from airflow_client.client.api.task_instance_api import TaskInstanceApi
from airflow_client.client.api.dag_api import DAGApi
from airflow_client.client.exceptions import ApiException
import os, requests
from airflow.sdk import Variable, timezone
from datetime import datetime

# logging setup
import logging
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)

#from include.constants import environment
environment = "LOCAL"
trigger_dag = "dag_km_waiting_dag"

def get_af_api_client():
    if environment == 'LOCAL':
        host = os.getenv("AIRFLOW_HOST", "http://host.docker.internal:8080")
        username = os.getenv("AIRFLOW_API_USERNAME") or Variable.get(
            "airflow_api_username", default="admin"
        )
        password = os.getenv("AIRFLOW_API_PASSWORD") or Variable.get(
            "airflow_api_password", default="admin"
        )
        headers = {"Content-Type": "application/json"}

        token_resp = requests.post(
            f"{host}/auth/token",
            json={"username": username, "password": password},
            timeout=30,
        )
        token_resp.raise_for_status()
        token = token_resp.json()["access_token"]

    else:
        host = os.getenv("AIRFLOW__HOST")
        api_token = f"API_TOKEN"
        token = os.getenv(api_token)

        if not host:
            raise RuntimeError("AIRFLOW__HOST is not set")
        if not token:
            raise RuntimeError(f"{api_token} is not set")

        if host.endswith("/api/v1") or host.endswith("/api/v2"):
            host = host.rsplit("/api/", 1)[0]

    configuration = airflow_client.client.Configuration(
        host=host,
        access_token=token
    )
    api_client = airflow_client.client.ApiClient(configuration)
    return api_client


def trigger_other_dag_via_api(context):
    #context = get_current_context()
    current_dag_id = context['dag'].dag_id
    logging.info(f"------- trigger DAG: {trigger_dag}")

    api_client = get_af_api_client()
    dag_api_instance = DAGApi(api_client)
    dag_run_api_instance = DagRunApi(api_client)

    logical_date = timezone.utcnow().isoformat()
    dag_run_api_instance.trigger_dag_run(
        dag_id=trigger_dag,
        trigger_dag_run_post_body={
            "dag_run_id": f"triggered__{logical_date}",
            "logical_date": logical_date,
            "conf": {
                "arg": "km",
            },
            "note": f"Triggered by DAG: {current_dag_id}",
        },
    )
    logging.info(f"DAG triggered: {trigger_dag}")

def km_function(**context):
    logging.info(f"Py function: km_function")
    logging.info("----------------- context -----------------")
    print_context(context)
    logging.info("----------------- context end -----------------")
    #logging.info("----current_context-----")
    #curr_context = get_current_context()
    #print_context(curr_context)


def dag_success_callback(context):
    logger.info("----------------- DAG Success -----------------")
    #context = get_current_context()
    print_context(context)
    #from pprint import pprint
    #pprint(context)


def dag_failure_callback(context):
    logger.info("----------------- DAG Failed -----------------")
    logger.error("----------------- DAG Failed -----------------")
    #context = get_current_context()
    #print_context(context)
    #from pprint import pprint
    #pprint(context)


def task_success_callback(context):
    logger.info("----------------- Task Success -----------------")
    #print_context(context)


def task_failure_callback(context):
    logger.info("----------------- Task failed -----------------")
    #print_context(context)


def print_context(context):
    for k,v in context.items():
        logging.info(f"*** {k} -> {v}")

def trigger_dag_via_api():
    context = get_current_context()
    trigger_other_dag_via_api(context)

args = {
    'owner': 'km',
    #'on_failure_callback': task_failure_callback,  #task level callback
    #'on_success_callback': trigger_other_dag_via_api   #task level callback
}

with DAG(
    dag_id='dag_callback_tests',
    default_args=args,
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    dagrun_timeout=timedelta(minutes=60),
    tags=['km'],
    params={"example_key": "example_value"},
    catchup=False,
    on_success_callback = trigger_other_dag_via_api,    #dag_success_callback,
    on_failure_callback = dag_failure_callback,
) as dag:

    py_task1 = PythonOperator(
        task_id='py_task1',
        python_callable=km_function,
        #default_args = args
    )

    py_task1
