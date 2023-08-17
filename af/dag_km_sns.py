from datetime import datetime, timedelta
import json,logging
import airflow, yaml
from airflow import DAG
#from airflow.operators.python_operator import PythonOperator
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator

# logging setup
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

job_run_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:00')
account_num = "123456"
region_name = "us-east-1"
topic_name = "km_test_sns"
subject = "Test SNS message Subject"
message = f"Test SNS message Body {job_run_timestamp}"

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

def send_sns_message(account_num, region_name, topic_name, subject, message, **kwargs):
    import boto3
    topic_arn='arn:aws:sns:'+region_name+':'+account_num+':'+topic_name
    try:
        sns = boto3.resource('sns',
            endpoint_url='https://sns.'+region_name+'.amazonaws.com',
            region_name=region_name
        )
        topic = sns.Topic(topic_arn)
        # publish to SNS
        #response = topic.publish(
        #    Subject=subject,
        #    Message=json.dumps({'default': message}),
        #    MessageStructure='json'
        #)
        response = topic.publish(
            Subject=subject,
            Message=message
        )
        ## using client (low level) & direct SMS
        #sns_client = boto3.client('sns')
        #sns_client.publish(PhoneNumber="+1234567890", Message="testing simple text")
        logging.info("Message sent to topic:"+topic_arn)
        logging.info("SNS response: "+json.dumps(response))
    except Exception as err:
        logging.info(f"Exception : {err}")
        if kwargs['task_instance'].try_number == 4:
            pass
        #raise Exception("Exception during division")



default_args = {
    'owner': 'km',
    'retries': 3,
    'start_date': airflow.utils.dates.days_ago(2),
    #'start_date': datetime.datetime(2021, 01, 01)
    'retry_delay': timedelta(seconds=10),
    'on_failure_callback': dag_failure_notification,
    'on_success_callback': dag_success_notification
}


with DAG('dag_km_sns', default_args=default_args, schedule_interval=None, catchup=False, dagrun_timeout=timedelta(minutes=90), tags=['km']) as dag:

    send_sns_message = PythonOperator(
        task_id='send_sns_message',
        python_callable=send_sns_message,
        provide_context=True,
        op_kwargs={
            'account_num': account_num,
            'region_name': region_name,
            'topic_name': topic_name,
            'subject': subject,
            'message': message,
        }
    )
    send_sns_message

if __name__ == "__main__":
    dag.cli()

