from datetime import datetime, timedelta
import logging, boto3, os, airflow, csv, json
import airflow.hooks.S3_hook
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.hooks.snowflake_hook import SnowflakeHook
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
from os import path


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#config
job_run_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:00')
date_for_file_name = datetime.now().strftime('%Y_%m_%d_%H_%M')
stage_loc = "/tmp/"
file_prefix = f"km_{datetime.now().strftime('%Y-%m-%d')}/"
file_name = f"test_{date_for_file_name}.csv"

aws_account = "1234"
snowflake_conn_id = "sf_conn_id"
bucket_name = "km-bkt"
region_name = "us-east-1"
# snowflake connection
sf_hook = SnowflakeHook(snowflake_conn_id=snowflake_conn_id, autocommit=False)
cs = sf_hook.get_cursor()
queue_name = "km_test_east1"

def save_data_to_s3(**kwargs):
    sql="DESC TABLE CONSOLIDATED_DAILY_OUTPUT;"
    #logging.info(f"Execute SQL: {sql}")
    #execute_sql(sql)
    #execute_sql_to_pandas_df(sql, stage_loc, file_name)
    create_file_and_send_to_s3(bucket_name, region_name, file_prefix, file_name)


def execute_sql(sql, **kwargs):
    """A function to run run SQL command in Snowflake."""
    cs.execute(sql)
    result = str(cs.fetchall())  #into single string
    logging.info(f"Result from SQL: {result}")
    logging.info(f"Result from SQL2: {result[0]}")


def execute_sql_to_sf_stage(sql, file_prefix, file_name, **kwargs):
    #create stage stg_km
    cs.execute(f"copy into @stg_km/{file_prefix}{file_name} from({sql}) file_format=ppa_csv HEADER=TRUE single=false max_file_size=4900000000")


def execute_sql_to_pandas_df(sql, stage_loc, file_name, **kwargs):
    """A function to run run SQL command in Snowflake."""
    cs.execute(sql)

    #df = cs.get_pandas_df(sql)  #'SnowflakeCursor' object has no attribute 'get_pandas_df'
    #df = cs.fetch_pandas_all() #'SnowflakeCursor' object has no attribute 'fetch_pandas_all'

    #for record in cs: print(f"{record[0]} - {record}") #prints as records
    #list_data = [record for record in cs]
    list_data = cs
    logging.info(f"Result from SQL: {list_data}")

    columns = ['name', 'type','kind','null?','default','primary key','unique key','check','expression','comment','policy name']
    import pandas as pd
    df = pd.DataFrame(list_data, columns=columns)
    print(f"Columns list: {df['name'].values.tolist()}")
    #df['name'].to_csv(stage_loc + file_name, index=False, header=True)
    #write_file_to_s3(bucket_name, file_prefix, stage_loc, file_name)

    #directly to S3
    import io
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    conn_s3 = boto3.resource('s3')
    conn_s3.Object(bucket_name, f"{file_prefix}{file_name}") \
        .put(Body=csv_buffer.getvalue()
             # , ServerSideEncryption='aws:kms', SSEKMSKeyId=kms_key
             )


def create_file_and_send_to_s3(bucket_name, region_name, file_prefix, file_name):
    s3 = boto3.resource("s3")
    bucket_ref = s3.Bucket(bucket_name)
    if list(bucket_ref.objects.filter(Prefix=file_prefix).limit(1)):
        logging.info(f"Skipping, as data file already exists: s3://{bucket_name}/{file_prefix}")
    else:
        create_test_file(stage_loc, file_name)
        if path.exists(stage_loc+file_name):
            write_file_to_s3(bucket_name, prefix=file_prefix, stage_loc=stage_loc, file_name=file_name)
            send_sns(aws_account, region_name=region_name, topic_name="km_test_sns", subject="File sent to S3", message=f"File sent to S3: {bucket_name}/{file_prefix}{file_name}")
            send_sqs(aws_account, region_name, queue_name, f"Data delivered to s3://{bucket_name}/{file_prefix}")
        else:
            logging.info(f"ERROR: No file found at: {stage_loc}{file_name}")


def create_test_file(dir_name, file_name):
    import pandas as pd
    data = [(1, 'aa', '2020-01-01'), (2, 'bb', '2021-01-01'), (3, 'cc', '2021-12-01')]
    dataDF = pd.DataFrame(data, columns=['id', 'name', 'login_date'])
    dataDF.to_csv(f"{dir_name}/{file_name}", sep="|", index=False, header=True)


def write_file_to_s3(bucket_name, prefix="km/", stage_loc="/tmp/", file_name=file_name):
    local_file_w_path = stage_loc + file_name

    if path.exists(local_file_w_path):
        logging.info(f"File: {local_file_w_path}; Upload to S3...")
        client = boto3.resource('s3')
        logging.info(f"Uploading file to bucket: {bucket_name}")
        client.Bucket(bucket_name).upload_file(stage_loc + file_name, prefix + file_name)
        os.remove(local_file_w_path)
        logging.info(f"Deleted file: {local_file_w_path}")
    else:
        logging.warning(f"File not found: {local_file_w_path}")


def send_sns(aws_account, region_name, topic_name, subject, message):
    topic_arn = 'arn:aws:sns:' + region_name + ':' + aws_account + ':' + topic_name
    sns = boto3.resource('sns',
                         endpoint_url=f"https://sns.{region_name}.amazonaws.com",
                         region_name=region_name,
                         )
    topic = sns.Topic(topic_arn)
    # publish to SNS
    response = topic.publish(
        Subject=subject,
        Message=json.dumps({'default': message}),
        MessageStructure='json'
    )


def send_sqs(aws_account, region_name, queue_name, message):
    logging.info(f"SQS: aws_account={aws_account} & region_name={region_name} && queue_name={queue_name} && ")
    queue_url = f"https://sqs.{region_name}.amazonaws.com/{aws_account}/{queue_name}"

    sqs = boto3.client("sqs", endpoint_url=f"https://sqs.{region_name}.amazonaws.com", region_name=region_name)
    response = sqs.send_message(QueueUrl=queue_url, MessageBody=message)

    print(f"response={response}")
    print(f"MessageId={response.get('MessageId')}")
    print(f"MD5OfMessageBody={response.get('MD5OfMessageBody')}")


def dag_success_notification(context, **kwargs):
    logger.info("DAG Success")


def dag_failure_notification(context, **kwargs):
    logger.info("DAG Failed")
    logger.error("DAG Failed")


default_args = {
    'owner': 'km',
    'start_date': airflow.utils.dates.days_ago(2),
    'retries': 3,
    'retry_delay': timedelta(seconds=10),
    'provide_context': True,
    'on_failure_callback': dag_failure_notification,
    'on_success_callback': dag_success_notification
}


with DAG('dag_km_data_to_s3', default_args=default_args, schedule_interval=None, catchup=False, dagrun_timeout=timedelta(minutes=90)) as dag:
    km_data_copy_task = PythonOperator(
        task_id='km_data_copy_task',
        python_callable=save_data_to_s3,
        trigger_rule="all_done",
        op_kwargs={
            'task_id': 'km_data_copy_task',
            "me": "km"
        }
    )
    #execute_file_task = SnowflakeOperator(
    #    task_id='execute_file_task',
    #    snowflake_conn_id=snowflake_conn_id,
    #    sql='my_sql_command.sql'
    #)

    km_data_copy_task
