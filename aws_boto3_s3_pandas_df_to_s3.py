import boto3
import os, io

#km1
access_key = ''
secret_key = ''

conn_s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)
#    region_name='us-east-1',

bucket_name="kmbkt"
file_dir_prefix="km/"
file_name_in_s3="km_file.csv"
#kms_key="kms-key-arn"


#pandas dataframe to s3
import pandas as pd

id='123'
name='jake'
load_date='2022-01-03'
data = [(id, name, load_date)]
data_df = pd.DataFrame(data, columns=['client', 'record_count', 'file_generation_date'])

#Option:1: stage df to local & upload file to s3
data_df.to_csv("/tmp/data_file.csv", index=False, header=True)

conn_s3.meta.client.upload_file("/tmp/data_file.csv",
                                bucket_name,
                                f"{file_dir_prefix}/{file_name_in_s3}"
                                #ExtraArgs={'ServerSideEncryption': 'aws:kms', 'SSEKMSKeyId': kms_key})
                                )
#or: conn_s3.Bucket(bucket_name).upload_file("/tmp/data_file.csv", f"{file_dir_prefix}/{file_name_in_s3}")

#option:2: write df directly to s3
#data_df.to_csv(f"s3://{bucket_name}/{file_dir_prefix}/{file_name_in_s3}", index=False, header=True)

csv_buffer = io.StringIO()
data_df.to_csv(csv_buffer, index=False)
conn_s3.Object(bucket_name, f"{file_dir_prefix}/{file_name_in_s3}")\
.put(Body=csv_buffer.getvalue()
         #, ServerSideEncryption='aws:kms', SSEKMSKeyId=kms_key
     )
