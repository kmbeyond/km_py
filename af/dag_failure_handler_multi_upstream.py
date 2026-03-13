from datetime import datetime
import random
import uuid

from airflow import DAG
from airflow.exceptions import AirflowFailException
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule


def km_function(**kwargs):
    print("Py function: km_function")

def km_task_success(**kwargs):
    print("SUCCESS")
    pass

def km_task_fail(**kwargs):
    print("FAILING")
    raise AirflowFailException(f"Random failure in task")

def km_function_random_fail(fail_probability: float = 0.5, **kwargs):
    ti = kwargs["ti"]
    job_run_id = str(uuid.uuid4())

    # Make job_run_id available even if we fail afterwards
    ti.xcom_push(key="job_run_id", value=job_run_id)

    r = random.random()
    print(f"task_id={ti.task_id} job_run_id={job_run_id} random={r} p_fail={fail_probability}")

    if r < fail_probability:
        raise AirflowFailException(f"Random failure in {ti.task_id}, job_run_id={job_run_id}")

    #return job_run_id  # stored as XCom 'return_value' when success

def send_caller_failure(profile, **context):
    raise RuntimeError(f"An upstream task failed for {profile}, marking the DAG as failed. Please check corresponding log task.")

def handle_failure( **kwargs):
    upstream_task_id = kwargs.get("upstream_task_id")
    ti = kwargs["ti"]
    job_run_id_xcomm = ti.xcom_pull(task_ids=upstream_task_id, key="job_run_id")
    job_run_id_param = kwargs["dbt_cloud_run_id"]
    print(f"Handling failure: job_run_id_xcomm={job_run_id_xcomm}, job_run_id_param={job_run_id_param}")


with DAG(
    dag_id="failure_handler_multi_upstream",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["km"],
) as dag:

    echo_params = PythonOperator(
        task_id="echo_params",
        python_callable=km_function,
    )

    primary_platform = PythonOperator(
        task_id="primary_platform",
        python_callable=km_task_fail,
        op_kwargs={"fail_probability": 0.5},
    )

    wait = EmptyOperator(task_id="wait")

    secondary_platform = PythonOperator(
        task_id="secondary_platform",
        python_callable=km_task_success,
        op_kwargs={"fail_probability": 0.5},
    )

    end = EmptyOperator(task_id="end")

    echo_params >> primary_platform >> wait >> secondary_platform >> end


    primary_failure_handler_task = PythonOperator(
        task_id="primary_failure_handler_task",
        python_callable=handle_failure,
        op_kwargs={"upstream_task_id": "primary_platform",
                   "dbt_cloud_run_id": "{{ task_instance.xcom_pull(task_ids='primary_platform', key='job_run_id') }}"},
        trigger_rule=TriggerRule.ALL_FAILED,  # runs only if primary_platform FAILED
    )
    primary_platform >> primary_failure_handler_task

    secondary_failure_handler_task = PythonOperator(
        task_id="secondary_failure_handler_task",
        python_callable=handle_failure,
        #dbt_cloud_run_id="{{ task_instance.xcom_pull(task_ids='secondary_platform', key='job_run_id') }}",
        op_kwargs={"upstream_task_id": "secondary_platform",
                   "dbt_cloud_run_id": "{{ task_instance.xcom_pull(task_ids='secondary_platform', key='job_run_id') }}"},
        trigger_rule=TriggerRule.ALL_FAILED,  # runs only if secondary_platform FAILED (not skipped)
    )
    secondary_platform >> secondary_failure_handler_task

    send_caller_failure_task = PythonOperator(
        task_id = "send_caller_failure_task",
        python_callable = send_caller_failure,
        op_kwargs={
            "profile": "km"
        },
        retries=0,
        trigger_rule=TriggerRule.ONE_FAILED
    )
    [ primary_platform, secondary_platform, primary_failure_handler_task, secondary_failure_handler_task ] >> send_caller_failure_task
