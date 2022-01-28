from datetime import datetime, timedelta
import logging, airflow, yaml
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from colorama import Fore

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

to_email_address = "km@gmail.com"
config_yaml_file = "config.yaml"

def dag_success_notification(context, **kwargs):
    logger.info("DAG Success")
    print_context(context)


def dag_failure_notification(context, **kwargs):
    logger.info("DAG Failed")
    logger.error("DAG Failed")
    print_context(context)


def print_context(context):
    for k,v in context.items():
        logging.info(f"{k} -> {v}")


def execute_metrics_report(config_yaml_file, to_email_address, **kwargs):
    """Calls snowflake stored procedure to get Monthly performance metrics into string"""
    #DAG config
    #config = yaml.load(open(config_yaml_file, 'r'), Loader=yaml.SafeLoader)
    #aws_account = config['aws_account']

    # snowflake connection
    snowflake_hook = SnowflakeHook(snowflake_conn_id="snowflake_conn_id_dev", autocommit=False)
    cs = snowflake_hook.get_cursor()
    #snowflake_hook_autocommit = SnowflakeHook(snowflake_conn_id=config['snowflake_conn_id'])
    #cs_autocommit = snowflake_hook_autocommit.get_cursor()
    logging.info("Calling: METRICS_REPORT_MONTHLY()")
    cs.execute(f"CALL METRICS_REPORT_MONTHLY('ppa')")
    result = str(cs.fetchall()[0][0])
    #result = str(snowflake_hook.get_first(f"CALL METRICS_REPORT_MONTHLY('ppa')"))
    logger.info(f"Result: {result}")



def my_args(*args, **kwargs):
    print(Fore.RED + "My Args are {}".format(args))
    print("My Kwargs are {}".format(kwargs))

def py_af_logging():
    from copy import deepcopy
    from airflow.config_templates.airflow_local_settings import DEFAULT_LOGGING_CONFIG

    LOGGING_CONFIG = deepcopy(DEFAULT_LOGGING_CONFIG)
    for k,v in LOGGING_CONFIG.items():
        logging.info(f"{k} -> {v}")

def py_exception_notify_4(to_email_address, *args, **kwargs):
    py_af_logging()
    divide_by_zero = 0
    try:
        result = 100/divide_by_zero
        logging.info(f"Division result: {result}")
    except Exception as err:
        logging.info(f"Exception during division: {err}")
        if kwargs['task_instance'].try_number == 4:
            #email
        raise Exception("Exception during division")


default_args = {
    'owner': 'airflow',
    'retries': 3,
    'start_date': airflow.utils.dates.days_ago(2),
    'retry_delay': timedelta(seconds=10),
    'on_failure_callback': dag_failure_notification,
    'on_success_callback': dag_success_notification
}
#    'start_date': datetime.datetime(2021, 09, 01) #airflow.utils.dates.days_ago(2),


with DAG('dag_km_test', default_args=default_args, schedule_interval=None, catchup=False, dagrun_timeout=timedelta(minutes=90)) as dag:

    dummy_task = DummyOperator(task_id='dummy_task')

    execute_metrics_report = PythonOperator(
        task_id='execute_metrics_report',
        python_callable=execute_metrics_report,
        provide_context = True,
        op_kwargs = {
            "config_yaml_file": config_yaml_file,
            'to_email_address': to_email_address,
        }
    )
    dummy_task >> execute_metrics_report

    bash_task = BashOperator(
        task_id='bash_task',
        bash_command='echo "Executing..."; echo "Airflow version:"`airflow version`; echo "Python:"`python -V`; echo "python3:"`python3 -V`; python3 -m pip list; exit 0'
    )
    dummy_task >> bash_task

    #py_args_test = PythonOperator(
    #    task_id='py_args_test',
    #    python_callable=my_args,
    #    op_args={'a','b','c'},
    #    op_kwargs={'a':'2'},
    #)
    #dummy_task >> py_args_test

    py_exception_notify_4 = PythonOperator(
        task_id='py_exception_notify_4',
        python_callable=py_exception_notify_4,
        provide_context=True,
        op_kwargs={
            'to_email_address': to_email_address,
        }
    )
    dummy_task >> py_exception_notify_4

