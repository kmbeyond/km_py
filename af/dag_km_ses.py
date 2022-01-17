from datetime import datetime, timedelta
import logging
import airflow.hooks.S3_hook
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
#from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.operators.bash_operator import BashOperator
#from airflow.operators.dummy_operator import DummyOperator
#from airflow.operators.email_operator import EmailOperator
import boto3
from botocore.config import Config

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
aws_account=""


def send_html_email(subject, body):
    print("aws_account:" + aws_account)
    config_ses = Config(
        retries={
            'max_attempts': 2,
            'mode': 'standard'
        }
    )
    ses_client = boto3.client("ses", region_name="us-east-1",
                              config=config_ses)
    #endpoint_url="email-smtp.us-east-1.amazonaws.com",
    response = ses_client.send_email(
        Destination={
            "ToAddresses": ["km@gmail.com"],
        },
        Message={
            "Body": {
                "Html": {
                    "Charset": "UTF-8",
                    "Data": body,
                }
            },
            "Subject": {
                "Charset": "UTF-8",
                "Data": subject,
            },
        },
        Source='km@gmail.com'
    )


def ppa_send_email():
    #result = str(snowflake_hook_autocommit.get_first(f"CALL MY_STORED_PROC()"))
    result = "<h3>welcome to SES email</h3>"
    try:
        send_html_email("SES test", result)
        print("SES Success")
    except:
        print("Failed to send using SES")
    else:
        print('Email sent! Message ID:')
        #print(response['MessageId'])

default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
    'retries': 3,
    'retry_delay': timedelta(minutes=0),
    'on_failure_callback': '',
    'on_success_callback': ''
}

with DAG('dag_km_ses', default_args=default_args, schedule_interval='0 12 1 * *', catchup=False,
         dagrun_timeout=timedelta(minutes=90)) as dag:

    bash_task = BashOperator(
        task_id='bash_task',
        bash_command="""echo "Welcome Let's start..." """
    )

    email_task = PythonOperator(
        task_id='email_task',
        python_callable=ppa_send_email
    )
    bash_task >> email_task

    #email_task = EmailOperator(
    #    task_id='email_task',
    #    to='km@gmail.com',
    #    subject='Airflow Alert',
    #   html_content=""" <h3>Email Test</h3> """,
    #)
    #execute_metrics_report_monthly_task >> email_task