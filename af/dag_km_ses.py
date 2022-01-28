from datetime import datetime, timedelta
import boto3, logging
import airflow.hooks.S3_hook
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from botocore.config import Config

# logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

to_email_address = "km@gmail.com"
ses_source_email = "km@gmail.com"

def send_html_email(ses_source_email, to_email_address, subject, body):
    #logger.info("aws_account:" + aws_account)
    config_ses = Config(
        retries={
            'max_attempts': 2,
            'mode': 'standard'
        }
    )
    ses_client = boto3.client("ses", region_name="us-east-1", config=config_ses)
    #endpoint_url="email-smtp.us-east-1.amazonaws.com",
    response = ses_client.send_email(
        Destination={
            "ToAddresses": [to_email_address],
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
        Source=ses_source_email
    )


def send_ses_email(to_email_address, ses_source_email, **kwargs):
    """Calls snowflake stored procedure to get Monthly performance metrics into string"""
    #result = str(snowflake_hook_autocommit.get_first(f"CALL METRICS_REPORT_MONTHLY()"))
    result = "<h3>welcome to SES email</h3>"
    try:
        send_html_email(ses_source_email, to_email_address, "SES test", result)
        logger.info("SES Success")
    except:
        logger.info("Failed to send using SES")
    else:
        logger.info('Email sent! Message ID:')
        #print(response['MessageId'])


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


default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
    'retries': 3,
    'retry_delay': timedelta(minutes=0),
    'on_failure_callback': dag_failure_notification,
    'on_success_callback': dag_success_notification
}

with DAG('dag_km_ses', default_args=default_args, schedule_interval=None, catchup=False, dagrun_timeout=timedelta(minutes=90)) as dag:

    email_task = PythonOperator(
        task_id='email_task',
        python_callable=send_ses_email,
        provide_context=True,
        op_kwargs={
            'to_email_address': to_email_address,
            'ses_source_email': ses_source_email
        }
    )
    email_task


