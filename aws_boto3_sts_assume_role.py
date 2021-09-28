import boto3
from botocore.config import Config
import logging
import json

#SETUP: Add Trust Relationship in Role for this user arn
def main():
    account_num = ''
    region_name = 'us-east-1'
    #km1
    access_key = ''
    secret_key = ''
    my_session = boto3.session.Session(aws_access_key_id=access_key,
                                       aws_secret_access_key=secret_key,
                                       region_name=region_name)
    print("Session established")
    role_name = ''
    session_name = "km_role_session_01"
    sts_client = my_session.client('sts')
    assumed_role_object = sts_client.assume_role(
        RoleArn="arn:aws:iam::"+account_num+":role/"+role_name,
        RoleSessionName=session_name
    )
    credentials = assumed_role_object['Credentials']
    print(f"credentials: {credentials}")
    s3_resource = boto3.resource(
        's3',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
    )
    #list all buckets if given access to s3:listBuckets
    #for bucket in s3_resource.buckets.all():
    #    print(bucket.name)
    my_bucket = s3_resource.Bucket('kiranbkt-development')
    for my_bucket_object in my_bucket.objects.all():
        print(f'->{my_bucket_object.key}')


if __name__ == "__main__":
    main()