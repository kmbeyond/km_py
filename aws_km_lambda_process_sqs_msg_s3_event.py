'''
#S3 event -> SQS -> Lambda
#pre steps


 -Attach "km_policy_access_to_s3" policy to Execution Role
 -Attach "km_policy_access_sqs" policy to Execution Role

Policy "km_policy_access_to_s3":
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AccessToS3",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::km-test-bucket",
                "arn:aws:s3:::km-test-bucket/*"
            ]
        }
    ]
}

Policy: km_policy_access_sqs
{
 "Version": "",
 "Statement": [
    {
    "Sid": "VisualEditor2",
    "Effect": "Allow",
    "Action": [ "sqs:DeleteMessage", "sqs:ReceiveMessage", "sqs:GetQueueAttributes" ],
    "Resource": "arn:aws:sqs:us-east-2:11111:km_test_sqs_east2"
    }
    ]

SQS message=
{"Records": [{"messageId": "aaaaa", "receiptHandle":"bbb", "body":"<<<<s3 event json>>>", "attributes": {.......}

S3 Event=
{"Records": [{"eventVersion": "2.1", "eventSource": "aws:s3", "awsRegion": "us-east-1", "eventTime": "2022-02-08T00:18:41.846Z", "eventName": "ObjectCreated:Put", "userIdentity": {"principalId": "AWS:xxx"}, "requestParameters": {"sourceIPAddress": "x.x.x.x"}, "responseElements": {"x-amz-request-id": "xxx", "x-amz-id-2": "xxxx"}, "s3": {"s3SchemaVersion": "1.0", "configurationId": "lambda_process_file", "bucket": {"name": "km-test-bucket", "ownerIdentity": {"principalId": "xxx"}, "arn": "arn:aws:s3:::km-test-bucket"}, "object": {"key": "km_ingestion/test_data_2022-01-28.csv", "size": 64, "eTag": "xxx", "sequencer": "006201B6E1CC1BA63D"}}}]}


'''

import json, boto3

def lambda_handler(event, context):
    print(f"KM event: {event}")
    #print(f"KM context: {context}")

    event_body = event.get("Records")[0].get("body")
    print(f"KM Event Body: {event_body}")
    event_body_json = json.loads(event_body)

    try:
        #bucket_name="km-bkt"
        bucket_name = event.get("Records")[0].get("s3").get("bucket").get("name")
        file_name_w_prefix = event_body_json.get("Records")[0].get("s3").get("object").get("key").replace("%3D","=")
        print(f"Event from: s3://{bucket_name}/{file_name_w_prefix}")

        #s3 = boto3.client('s3')
        #data = s3.get_object(Bucket=bucket_name, Key=file_name_w_prefix)
        #contents_binary = data['Body'].read()
        #contents_text = contents_binary.decode('utf-8')
        #print(f"File contents: {contents_text}")
        #for line in contents_text.split('\n'):
        #    print(f"-> {line}")
        #    #process each line

        #processed_file_dir_prefix="km_lambda_processed/"
        #print(f"File copy to: s3://{bucket_name}/{processed_file_dir_prefix}{file_name_w_prefix}")
        #s3 = boto3.resource("s3")
        #s3.meta.client.move({'Bucket': bucket_name, 'Key': file_name_w_prefix},
        # bucket_name,
        # processed_file_dir_prefix+file_name_w_prefix
        #)

        #s3.Object(bucket_name, f"{processed_file_dir_prefix}{file_name_w_prefix}").copy_from(CopySource=bucket_name+'/'+file_name_w_prefix)
        #s3.Object(bucket_name, file_name_w_prefix).delete()

        #delete message from queue
        aws_account = "11111"
        region_name = "us-east-2"
        queue_name = "km_test_sqs_east2"
        receipt_handle = event.get("records")[0].get("receiptHandle")
        sqs = boto3.client("sqs", endpoint_url=f"https://sqs.{region_name}.amazonaws.com", region_name=region_name)
        queue_url = f"https://queue.amazonaws.com/{aws_account}/{queue_name}"
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
        print(f"Deleted message")
        statusCode=200
        status_body = "Completed"

    except Exception as err:
        receipt_handle = event.get("records")[0].get("receiptHandle")
        error_message = f"KM Exception with message ({receipt_handle}: {err}"
        statusCode = 4200
        status_body = error_message
    finally:
        pass
    return {
        'statusCode': statusCode,
        'body': json.dumps(f'Data sent to {status_body}')
    }
