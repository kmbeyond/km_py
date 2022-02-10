from datetime import datetime, timedelta
import logging, boto3, os, airflow, csv, json
import airflow.hooks.S3_hook
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#config
#job_run_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:00')
aws_account = "123"
region_name = "us-east-1"
proxy_server = "http://proxy.km.com:1234"


def send_sqs_dummy(aws_account, region_name, queue_name, message):
    logging.info(f"Dummy send: SQS: {queue_name}")


def send_sqs(aws_account, region_name, queue_name, message, **kwargs):
    logging.info(f"SQS: aws_account={aws_account} & region_name={region_name} && queue_name={queue_name} && ")
    queue_url = f"https://sqs.{region_name}.amazonaws.com/{aws_account}/{queue_name}"

    #sqs = boto3.client("sqs", endpoint_url=f"https://sqs.us-east-1.amazonaws.com", region_name="us-east-1")
    sqs = boto3.client("sqs", endpoint_url=f"https://sqs.{region_name}.amazonaws.com", region_name=region_name)
    response = sqs.send_message(QueueUrl=queue_url, MessageBody=message)

    #from botocore.config import Config
    #proxy_config = Config(
    #    proxies={
    #        'http': proxy_server, #config['proxy_server'],
    #        'https': proxy_server #config['proxy_server']
    #    }
    #)
    #sqs_proxy = boto3.resource("sqs", config=proxy_config)
    #response = sqs_proxy.get_queue_by_name(QueueName=queue_name).send_message(MessageBody=message)

    print(f"response={response}")
    print(f"MessageId={response.get('MessageId')}")
    print(f"MD5OfMessageBody={response.get('MD5OfMessageBody')}")


def km_poll_sqs_messages(aws_account, region_name, queue_name, **kwargs):
    logging.info(f"Poll SQS Queue: {queue_name}")

    sqs = boto3.client("sqs", endpoint_url=f"https://sqs.{region_name}.amazonaws.com", region_name=region_name)
    queue_url = f"https://queue.amazonaws.com/{aws_account}/{queue_name}"
    resp = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10, VisibilityTimeout=0)
    for itm in resp['Messages']:
        receipt_handle = itm['ReceiptHandle']
        logging.info(f"----> {itm}")
        logging.info(f"----> {itm.get('Body')}")
        #sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
        #logging.info(f"----> Deleted receipt_handle: {receipt_handle}")


def dag_success_notification(context, **kwargs):
    logger.info("DAG Success")


def dag_failure_notification(context, **kwargs):
    logger.info("DAG Failed")
    logger.error("DAG Failed")
    print_context(context)

def print_context(context):
    for k,v in context.items():
        logging.info(f"{k} -> {v}")

default_args = {
    'owner': 'km',
    'start_date': airflow.utils.dates.days_ago(2),
    'retries': 3,
    'retry_delay': timedelta(seconds=10),
    'provide_context': True,
    'on_failure_callback': dag_failure_notification,
    'on_success_callback': dag_success_notification
}


with DAG('dag_km_sqs', default_args=default_args, schedule_interval=None, catchup=False, dagrun_timeout=timedelta(minutes=90)) as dag:
    send_sqs = PythonOperator(
        task_id='send_sqs',
        python_callable=send_sqs,
        trigger_rule="all_done",
        op_kwargs={
            #'task_id': 'send_sqs',
            'aws_account': aws_account,
            "region_name": region_name,
            "queue_name": "km_test_east1",
            "message": f"data sent at {datetime.now().strftime('%Y-%m-%d %H:%M:00')}"
        }
    )

    km_poll_sqs_messages = PythonOperator(
        task_id='km_poll_sqs_messages',
        python_callable=km_poll_sqs_messages,
        trigger_rule="all_done",
        op_kwargs={
            'aws_account': aws_account,
            "region_name": region_name,
            "queue_name": "km_test_east1"
        }
    )
    send_sqs >> km_poll_sqs_messages
