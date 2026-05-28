from datetime import datetime
import pendulum
from airflow import DAG
from airflow.exceptions import AirflowFailException
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.python import PythonSensor
from airflow.models import Variable, DagBag, DagRun, DagTag, TaskInstance
#from airflow.utils.session import provide_session
from airflow.utils.session import create_session

def check_running_dags_by_tags(tag_names, dag_id, match_mode, session=None, **context):
    """
    Checks if there are any other active DAG runs (excluding the current DAG) that have the specified tags and at least one running task (excluding 'check_running_dags').
    Supports 'AND' mode (all tags must be present) and 'OR' mode (any tag present).
    Returns True if no such DAGs are running, otherwise False.

    Args:
        tag_names (list): List of tag names to check.
        dag_id (str): The current DAG ID to exclude.
        match_mode (str): 'AND' for all tags, 'OR' for any tag.
        session: SQLAlchemy session (provided by Airflow).
        **context: Airflow context dictionary.

    Returns:
        bool: True if no other matching DAGs are running, False otherwise.
    """
    if session is None:
        with create_session() as new_session:
            return check_running_dags_by_tags_callable(
                tag_names, dag_id, match_mode, session=new_session, **context
            )
    query = (
        session.query(DagRun.dag_id)
            .join(DagTag, DagRun.dag_id == DagTag.dag_id)
            .filter(DagTag.name.in_(tag_names))
            .filter(DagRun.state == State.RUNNING)
            .filter(DagRun.dag_id != dag_id)
            .filter(~DagRun.dag_id.like('%dq%'))  # Exclude DAGs with 'dq' in their ID
            .filter(~exists().where(
            (TaskInstance.run_id == DagRun.run_id) &
            (TaskInstance.task_id == 'check_running_dags') &
            (TaskInstance.state.in_([State.RUNNING, State.UP_FOR_RESCHEDULE]))
        ).correlate(DagRun))
    )

    if match_mode == 'AND':
        query = query.group_by(DagRun.dag_id).having(func.count(func.distinct(DagTag.name)) == len(tag_names))
    else:
        query = query.distinct()

    print(str(query.statement.compile(compile_kwargs={"literal_binds": True})))
    running_dags = query.all()
    print(f"running_dags: {running_dags}")

    if running_dags:
        dag_ids = [r[0] for r in running_dags]
        print(f"RUNNING DAGs (tags: '{tag_names}' & match-mode: '{match_mode}' ): {dag_ids}")
        return False
    else:
        print(f"NO RUNNING DAGs (tags: '{tag_names}' & match-mode: '{match_mode}' )")
        return True

timeout = 3600
mode = 'reschedule'
tag_names = ["km", "km_dag_triggers", ]
match_mode = "OR"

with DAG(
    dag_id="dag_km_check_running_dags_by_tags",
    #start_date=datetime(2025, 1, 1),
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    max_active_runs=1,
    tags=["km"],
) as dag:

    start = EmptyOperator(task_id="start")

    check_running_dags = PythonSensor(
            task_id = "check_running_dags",
            poke_interval = 60,           # Check every 60 seconds
            timeout = timeout,            # Timeout after 1 hour
            mode = mode,                  # Free up worker slots when not poking
            python_callable = check_running_dags_by_tags,
            op_kwargs = {
                'tag_names': tag_names,
                'dag_id': dag.dag_id,
                'match_mode': match_mode
            }
        )

    end = EmptyOperator(task_id="end")

    start >> check_running_dags >> end


