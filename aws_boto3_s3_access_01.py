import boto3
import os

#km1
access_key = ''
secret_key = ''

conn_s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)
#    region_name='us-east-1',

#buckets list
for bucket in conn_s3.buckets.all():
    print(bucket.name)

#Download data from a bucket
bkt_name='kiranbkt'
path_local_files='/home/km/km/km_pr/aws/data_from_s3/'
#items in a bucket
bkt_obj = conn_s3.Bucket(bkt_name)
for obj in bkt_obj.objects.all():
    #print(f"-> {obj}")
    if obj.key[-1] != '/' and obj.key[-1] != '$':
        file = obj.key
        path, filename = os.path.split(obj.key)
        filename = os.path.basename(file)
        print(f"FILE: {obj.key} -> {path}  -> {filename}")
        # download files with NO directory path
        # dest_file = os.path.join(path_local_files, filename)
        # print(f" --------> {dest_file}")
        # bkt_obj.download_file(obj.key, dest_file)
        # download files with directories
        dest_file_w_dir = os.path.join(path_local_files, obj.key)
        if not os.path.exists(os.path.dirname(dest_file_w_dir)):
            os.makedirs(os.path.dirname(dest_file_w_dir))
        print(f" --------> {dest_file_w_dir}")
        bkt_obj.download_file(obj.key, dest_file_w_dir)


#obj.key.endswith("/")

