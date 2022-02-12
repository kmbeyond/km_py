'''
#pre steps

km_lambda_process_s3_notification
 -Attach "km-policy-access-to-s3" policy to Execution Role

Policy "km-policy-access-to-s3":
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

Event=
{"Records": [{"eventVersion": "2.1", "eventSource": "aws:s3", "awsRegion": "us-east-1", "eventTime": "2022-02-08T00:18:41.846Z", "eventName": "ObjectCreated:Put", "userIdentity": {"principalId": "AWS:xxx"}, "requestParameters": {"sourceIPAddress": "x.x.x.x"}, "responseElements": {"x-amz-request-id": "xxx", "x-amz-id-2": "xxxx"}, "s3": {"s3SchemaVersion": "1.0", "configurationId": "lambda_process_file", "bucket": {"name": "km-test-bucket", "ownerIdentity": {"principalId": "xxx"}, "arn": "arn:aws:s3:::km-test-bucket"}, "object": {"key": "km_lambda/test_data_2022-01-28.csv", "size": 64, "eTag": "xxx", "sequencer": "006201B6E1CC1BA63D"}}}]}


'''

import json, boto3,os

def lambda_handler(event, context):
    print(f"Event: {event}")
    print(f"context: {context}")
    #bucket_name="km-test-bucket-ppa"
    bucket_name = event.get("Records")[0].get("s3").get("bucket").get("name")
    file_name_w_prefix = event.get("Records")[0].get("s3").get("object").get("key")
    print(f"Event from: s3://{bucket_name}/{file_name_w_prefix}")
    
    s3 = boto3.client('s3')
    data = s3.get_object(Bucket=bucket_name, Key=file_name_w_prefix)
    contents = data['Body'].read()
    print(f"File contents: {contents}")

    processed_file_dir_prefix="km_lambda_processed/"
    print(f"File copy to: s3://{bucket_name}/{processed_file_dir_prefix}{file_name_w_prefix}")
    s3 = boto3.resource("s3")
    #s3.meta.client.move({'Bucket': bucket_name, 'Key': file_name_w_prefix},
    # bucket_name,
    # processed_file_dir_prefix+file_name_w_prefix
    #)
    
    s3.Object(bucket_name, f"{processed_file_dir_prefix}{file_name_w_prefix}").copy_from(CopySource=bucket_name+'/'+file_name_w_prefix)
    s3.Object(bucket_name, file_name_w_prefix).delete()
    print(f"-> Completed")
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Data sent to {bucket_name}')
    }
