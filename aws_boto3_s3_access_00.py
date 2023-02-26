
import boto3
import io

#boto3.client('sts').get_caller_identity()

bucket_name = "xx"

#-------------using client

s3_client = boto3.client('s3')
bkt =  s3_client.list_objects_v2(Bucket=bucket_name) 
for obj in bkt['Contents']:
  print("FILE:", obj['Key'])

obj = s3_client.get_object(Bucket=bucket_name, Key='2023-01-21/dummy.txt')

#read into pandas df
df = pd.read_csv(obj.get("Body"))

#read as IO bytes
#df = pd.read_csv(io.BytesIO(obj["Body"].read()), low_memory=False)

df.head(10)


#--------------using resource
s3 = boto3.resource(service_name='s3')
bkt = s3.Bucket(bucket_name)
for obj in bkt.objects.all():
  print("FILE:", obj.key)

 s3_resource = boto3.resource(service_name='s3')

#bkt = s3_resource.Bucket(bucket_name)

obj = s3_resource.Object(bucket_name=bucket_name, key='2023-01-21/dummy.txt')

df = pd.read_csv(obj.get()['Body'])
df.head(10)


