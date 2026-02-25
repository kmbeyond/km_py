from airflow import DAG, Dataset
from airflow.utils.dates import days_ago
from airflow.utils.trigger_rule import TriggerRule
from airflow import DAG, Dataset
from airflow.operators.python import PythonOperator
from airflow.providers.dbt.cloud.operators.dbt import (
    DbtCloudRunJobOperator,
    DbtCloudGetJobRunArtifactOperator,
)
import logging
#from airflow.providers.http.hooks.http import HttpHook
#from airflow.models import Variable
from airflow.providers.dbt.cloud.hooks.dbt import DbtCloudHook

dbt_cloud_conn_id = "km_af_conn" #airflow connection to dbt cloud (Acc#, url, pat, ...)
dbt_cloud_job_id = "12345678"

def read_artifacts_file_for_run_id(file_name, max_lines: int = 500, **context) -> None:
    ti = context["ti"]
    run_id = ti.xcom_pull(task_ids="km_run_dbt_job", key="job_run_id")
    file_name_full = f"{run_id}_{file_name}"
    import os
    if not os.path.exists(file_name_full):
        raise FileNotFoundError(
            f"Expected log file not found: {file_name_full}. "
            "This usually means the artifact wasn't written locally or task ran on a different worker."
        )
    with open(file_name_full, "r", encoding="utf-8") as f:
        print("------------------------------------------------------------")
        print(f"***** Reading local artifact file: {file_name}")
        for i, line in enumerate(f):
            if i >= max_lines:
                print(f"... truncated after {max_lines} lines ...")
                break
            print(line.rstrip("\n"))
        print("------------------------------------------------------------")
    #with open(file_name_full, "r", encoding="utf-8", errors="replace") as f:
    #    for line in f:
    #        # don't double-add newlines
    #        log.info(line.rstrip("\n"))

def print_dbt_log_file(**context) -> None:
    hook = DbtCloudHook(dbt_cloud_conn_id = dbt_cloud_conn_id)
    ti = context["ti"]
    log = logging.getLogger("airflow.task")

    run_id = ti.xcom_pull(task_ids="km_run_dbt_job", key="job_run_id")
    if not run_id:
        raise ValueError("job_run_id not found in XCom from km_run_dbt_job")

    artifact_content = hook.get_job_run_artifact(run_id=run_id, path="dbt.log")

    log.info("------------------------------------------------------------")
    log.info(artifact_content)
    log.info("------------------------------------------------------------")


with DAG(
    dag_id="km_test_dbt_job_run",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
    tags=["km"],
    max_active_runs=1,
    default_args={'owner': 'km'}

) as dag:

    km_run_dbt_job = DbtCloudRunJobOperator(
        task_id = task_id,
        dbt_cloud_conn_id = dbt_cloud_conn_id,
        job_id = dbt_cloud_job_id,
        check_interval = 30,
        timeout = 3600,
        outlets = [ Dataset("/ts/km_model1") ],
        steps_override = [
            "dbt run --select km_dbt1"
        ],
        retries = 3,
        retry_delay = timedelta(minutes=5),
        retry_from_failure = True
    )

    get_run_results = DbtCloudGetJobRunArtifactOperator(
        task_id = "get_run_results_artifact",
        dbt_cloud_conn_id = dbt_cloud_conn_id,
        run_id = "{{ ti.xcom_pull(task_ids='km_run_dbt_job', key='job_run_id') }}",
        path = "run_results.json",   #artifacts metadata
        #path = "dbt.log"   #file not exists
    )

    read_artifacts_file = PythonOperator(
        task_id = 'read_artifacts_file',
        python_callable = read_artifacts_file_for_run_id,
        provide_context = True,
        op_kwargs = {
            "file_name": "run_results.json",
            "max_lines": 1000
        }
    )

    print_run_output = PythonOperator(
        task_id = "print_dbt_cloud_run_output",
        python_callable = print_dbt_log_file,
        provide_context = True,
        op_kwargs = { },
    )

    km_run_dbt_job >> get_run_results >> read_artifacts_file >> print_run_output
