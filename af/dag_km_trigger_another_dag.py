from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import Variable, timezone
from datetime import datetime
import os, requests

import airflow_client.client
from airflow_client.client.api.dag_run_api import DagRunApi
from airflow_client.client.api.task_instance_api import TaskInstanceApi
from airflow_client.client.api.dag_api import DAGApi
from airflow_client.client.exceptions import ApiException

# logging setup
import logging
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)

def get_af_api_client():
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

    headers["Authorization"] = f"Bearer {token}"
    url = f"{host}/api/v2/dags"
    response = requests.get(url, headers=headers)
    #print(f"response: {response.json()}")

    configuration = airflow_client.client.Configuration(
        host=host,
        access_token=token
    )
    api_client = airflow_client.client.ApiClient(configuration)
    return api_client


def trigger_other_dag_via_api(child_dag, **context):
    current_dag_id = context['dag'].dag_id

    api_client = get_af_api_client()
    dag_api_instance = DAGApi(api_client)
    dag_run_api_instance = DagRunApi(api_client)

    logical_date = timezone.utcnow().isoformat()
    dag_run_api_instance.trigger_dag_run(
        dag_id=child_dag,
        trigger_dag_run_post_body={
            "dag_run_id": f"triggered__{logical_date}",
            "logical_date": logical_date,
            "conf": {
                "arg": "km",
            },
            "note": "Triggered by km",
        },
    )
    logging.info(f"DAG triggered: {child_dag}")

    """
    resp = requests.post(
        f"{host}/api/v2/dags/{child_dag}/dagRuns",
        json={"conf": {"source": f"{current_dag_id}"}},
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()
    """

with DAG(
    dag_id="dag_km_trigger_another_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['km', 'km_dag_triggers']
) as dag:

    trigger_task = PythonOperator(
        task_id="trigger_child_via_http",
        python_callable=trigger_other_dag_via_api,
        op_kwargs = {
           "child_dag": "dag_km_waiting_dag"
        }
    )
