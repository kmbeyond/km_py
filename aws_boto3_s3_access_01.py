import boto3
import os

#km
access_key = ''
secret_key = ''

conn_s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)
#    region_name='us-east-1',

print(f"-- all buckets list")
for bucket in conn_s3.buckets.all():
    print(f"-> {bucket}")
print(f"-----")

#Download data from a bucket
bkt_name = 'kiranbkt'
path_local_files = '/home/km/km/km_practice/aws/data_from_s3/'


def list_files(bkt_name, prefix=""):
    # items in a bucket
    bkt_obj = conn_s3.Bucket(bkt_name)
    if prefix == "":
        return bkt_obj, bkt_obj.objects.all()
    else:
        return bkt_obj, bkt_obj.objects.filter(Prefix=prefix)


bkt_obj, obj_list = list_files(bkt_name)
for obj in obj_list:
    print(f"-> {obj}")


print("-- Listing Files in Finance --")
bkt_obj, obj_list = list_files(bkt_name, "Finance")
for obj in obj_list:
    print(f"-> {obj}")


def download_files(bkt_name, path_local_files, prefix=""):
    #Get items in bucket
    bkt_obj, obj_list = list_files(bkt_name, prefix)

    for obj in obj_list:
        print(f"-> {obj}")
        #Check if dir or log dir
        if obj.key[-1] == '/' or obj.key[-1] == '$':
            print(f" ---> skipping")
        else:
            file = obj.key
            path, filename = os.path.split(obj.key)
            filename = os.path.basename(file)
            print(f"FILE: {obj.key} -> {path}  -> {filename}")

            # download files with directories
            dest_file_w_dir = os.path.join(path_local_files, obj.key)
            if not os.path.exists(os.path.dirname(dest_file_w_dir)):
                print(f" ---> Dir creating: {os.path.dirname(dest_file_w_dir)}")
                os.makedirs(os.path.dirname(dest_file_w_dir))
            print(f" ---> Downloading: {dest_file_w_dir}")
            bkt_obj.download_file(obj.key, dest_file_w_dir)

            # download just files (NOT directory path)
            #dest_file = os.path.join(path_local_files, filename)
            #print(f" ---> Downloading {dest_file}")
            #bkt_obj.download_file(obj.key, dest_file)


print("-- Downloading Files from Bucket:")
#download_files(bkt_name, path_local_files)

#download_files(bkt_name, path_local_files, prefix="Finance")

