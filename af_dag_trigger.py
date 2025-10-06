import json, requests, boto3, os, yaml
from botocore.exceptions import ClientError


AIRFLOW_URL = "https://xxx.astronomer.run/xx/api/v1/dags"
astro_api_token = "xxx"

session = boto3.session.Session()

def send_sns_notification(subject, message, topic_arn):
    sns = boto3.client('sns', region_name="us-east-1")
    sns.publish(
        TopicArn=topic_arn,
        Subject=subject,
        Message=message
    )
    print("SNS notification sent")


# Load schema mapping at cold start
with open("./lambda_event_dag_mapping.yml", "r") as f:
    SCHEMA_MAPPING = yaml.safe_load(f)

def lambda_handler(event, context):

    SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")  # Set this env var to your SNS topic ARN

    for record in event['Records']:
        print(f"Payload is: {record['body']}")
        try:
            body = json.loads(record['body'])
        except Exception as e:
            print(f"Error parsing record['body'] as JSON: {e}")
            if SNS_TOPIC_ARN:
                subject = f"ERROR Lambda JSON Load Error"
                message = f"Failed to parse record['body'] as JSON.\n\nError: {e}\n\nPayload:\n{record['body']}"
                send_sns_notification(subject, message, SNS_TOPIC_ARN)
            continue
        print(f"Received message: {body}")

        # If SNS-wrapped, extract and parse the actual message
        if 'Message' in body:
            try:
                actual_msg = json.loads(body['Message'])
            except Exception as e:
                print(f"Error parsing body['Message'] as JSON: {e}")
                if SNS_TOPIC_ARN:
                    subject = f"{ENVIRONMENT} - [ALERT] Lambda SNS Message JSON Load Error"
                    message = f"Failed to parse body['Message'] as JSON.\n\nError: {e}\n\nbody['Message']:\n{body['Message']}"
                    send_sns_notification(subject, message, SNS_TOPIC_ARN)
                continue
        else:
            actual_msg = body

        dag_event = actual_msg.get('dag_id', 'yyy').lower()

        # Replace schema_name if mapping exists
        if dag_event in SCHEMA_MAPPING:
            mapped_dag = SCHEMA_MAPPING[dag_event].get('dag_id', 'zzz')
        else:
            print(f"No mapping found for DAG event {dag_event}")
            print(f"Skipping DAG trigger for DAG event {dag_event}")
            continue

        # Construct the DAG ID
        dag_id = f"{target_db}__{mapped_dag}"
        airflow_api_url = f"{AIRFLOW_URL}/{dag_id}/dagRuns"

        # Prepare conf payload for Airflow
        conf = {
            "receipt_handle": receipt_handle,
            **actual_msg  # Pass all message fields if needed
        }

        headers = {
            "Authorization": f"Bearer {astro_api_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "conf": conf
        }

        # Trigger the DAG via Astro's Airflow REST API
        print("Calling Airflow API to trigger DAG...")
        response = requests.post(airflow_api_url, headers=headers, data=json.dumps(payload))
        print(f"Triggered DAG {dag_id}: {response.status_code} {response.text}")

        # If DAG not found or any error, send SNS notification
        if response.status_code != 200 and SNS_TOPIC_ARN:
            if response.status_code == 404:
                subject = f"{ENVIRONMENT} - [ALERT] Airflow DAG Not Found: {dag_id}"
                message = f"The following DAG could not be found in Airflow:\n\nDAG ID: {dag_id}\n\nResponse:\n{response.text}"
            else:
                subject = f"{ENVIRONMENT} - [ALERT] Airflow DAG Trigger Failed: {dag_id}"
                message = f"Failed to trigger DAG in Airflow.\n\nDAG ID: {dag_id}\nStatus Code: {response.status_code}\nResponse:\n{response.text}"
            send_sns_notification(subject, message, SNS_TOPIC_ARN)


    return {"status": "done"}
