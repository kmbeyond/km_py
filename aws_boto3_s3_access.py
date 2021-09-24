

import boto3

access_key = 'AKIAVP2HFGCVOUOKINV6'
secret_key = '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'

conn_s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

for bucket in conn_s3.buckets.all():
    print(bucket.name)
