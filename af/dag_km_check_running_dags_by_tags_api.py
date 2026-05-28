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
from airflow_client.client.models import PatchTaskInstanceBody

# logging setup
import logging
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)
wait_for_seconds = 60

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


def see_dag_runs_api(tag_names, match_mode, **context):
    current_dag_id = context['dag'].dag_id

    api_client = get_af_api_client()
    dag_api_instance = DAGApi(api_client)
    dag_run_api_instance = DagRunApi(api_client)
    task_instance_api_instance = TaskInstanceApi(api_client)

    #logical_date = timezone.utcnow().isoformat()
    offset = 0
    page_size = 100  # Airflow API commonly caps this endpoint at 100 rows/page.
    dag_page = dag_api_instance.get_dags(
        limit=page_size,
        offset=offset,
        tags=list(set(tag_names or [])),
        tags_match_mode='all' if match_mode.lower() == 'and' else 'any',
        dag_run_state=['running']
    )
    dags_obj = dag_page.dags or []
    dags_running = [dag_obj.dag_id for dag_obj in dags_obj if dag_obj.dag_id != current_dag_id]
    logging.info(f"Running DAGs: {dags_running}")

    for running_dag_id in dags_running:
        logging.info(f"----DAG: {running_dag_id}")
        dag_runs = dag_run_api_instance.get_dag_runs(
            dag_id=running_dag_id,
            state=["running"]
        )
        logging.info(f"Waiting for : {wait_for_seconds} seconds")
        import time
        time.sleep(wait_for_seconds)
        logging.info(f" ---> Wake Up to check for running instances of {running_dag_id}")

        for dag_run in dag_runs.dag_runs:
            tis = task_instance_api_instance.get_task_instances(
                dag_id=running_dag_id,
                dag_run_id=dag_run.dag_run_id
            )

            active_tasks = [
                ti.task_id for ti in tis.task_instances
                if ti.state in ["running", "queued", "up_for_reschedule"]
            ]
            logging.info(f" --> tasks: {running_dag_id}/{active_tasks}")
            if len(active_tasks)==0:
                logging.info(f"NO Task running")


def get_dag_runs_count_api(check_dag_id, **context):
    current_dag_id = context['dag'].dag_id

    api_client = get_af_api_client()
    dag_api_instance = DAGApi(api_client)
    dag_run_api_instance = DagRunApi(api_client)
    task_instance_api_instance = TaskInstanceApi(api_client)
    #logging.info([m for m in dir(DagRunApi) if "task" in m.lower() or "instance" in m.lower()])
    #logging.info([m for m in dir(TaskInstanceApi) if "task" in m.lower() or "instance" in m.lower()])
    #logging.info([m for m in dir(task_instance_api_instance) if "task" in m.lower() or "instance" in m.lower()])
    #import inspect
    #logging.info(inspect.signature(task_instance_api_instance.patch_task_instance))
    logging.info(inspect.signature(dag_run_api_instance.patch_dag_run))

    offset = 0
    page_size = 100  # Airflow API commonly caps this endpoint at 100 rows/page.
    dag_page = dag_api_instance.get_dags(
        limit=page_size,
        offset=offset,
        dag_id_pattern = check_dag_id,
        dag_run_state=['running', 'queued']
    )
    dags_obj = dag_page.dags or []
    dags_running = [dag_obj.dag_id for dag_obj in dags_obj if dag_obj.dag_id != current_dag_id]
    logging.info(f"Running DAGs: {dags_running}")
    ACTIVE_STATES = {
        "running",
        "queued",
        "scheduled",
        "up_for_retry",
        "up_for_reschedule",
        "deferred",
    }
    for running_dag_id in dags_running:
        logging.info(f"----DAG: {running_dag_id}")
        dag_runs = dag_run_api_instance.get_dag_runs(
            dag_id=running_dag_id,
            state=["running"]
        )
        dags_list = [dag_run.dag_run_id for dag_run in dag_runs.dag_runs]
        dag_runs_count = len(dags_list)
        logging.info(f" --> Run Count : {dag_runs_count}  --> {dags_list}")

        if dag_runs_count>=1:
            logging.info("Mark all as Success:")
            mark_dag_status_body = {"state": "failed"}
            for dag_run_id in dags_list:
                logging.info(f" Dag run: {dag_run_id}")
                tis = task_instance_api_instance.get_task_instances(
                    dag_id=running_dag_id,
                    dag_run_id=dag_run_id
                )
                for ti in tis.task_instances:
                    #logging.info(f"  --> {ti.task_id} - {ti.state}")
                    if ti.state in ACTIVE_STATES:
                        logging.info(
                            f" --> Mark task: {running_dag_id}/{dag_run_id}/{ti.task_id} state={ti.state}"
                        )
                        task_instance_api_instance.patch_task_instance(
                            dag_id=running_dag_id,
                            dag_run_id=dag_run_id,
                            task_id=ti.task_id,
                            patch_task_instance_body = PatchTaskInstanceBody(state="success")
                        )
                logging.info(f" --> Mark dag run: {running_dag_id}/{dag_run_id}")
                dag_run_api_instance.patch_dag_run(
                    dag_id=running_dag_id,
                    dag_run_id=dag_run_id,
                    dag_run_patch_body= airflow_client.client.models.dag_run_patch_body.DAGRunPatchBody(state="success")
                )


def mark_task_instance_success(task_instance_api_instance, dag_id, dag_run_id, task_id):

    return task_instance_api_instance.patch_task_instance(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        #update_mask=["state"],   # keep if your client expects it
        body={"state": "success"},
    )


with DAG(
    dag_id="dag_km_check_running_dags_by_tags_api",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['km', 'km_dag_triggers']
) as dag:

    see_dag_runs_task = PythonOperator(
        task_id="see_dag_runs_task",
        python_callable=see_dag_runs_api,
        op_kwargs = {
            "tag_names": ["km"],
            "match_mode": "OR"
        }
    )
    get_dag_runs_count_task = PythonOperator(
        task_id="get_dag_runs_count_task",
        python_callable=get_dag_runs_count_api,
        op_kwargs={
            "check_dag_id": "dag_km_waiting_dag"
        }
    )

    get_dag_runs_count_task
