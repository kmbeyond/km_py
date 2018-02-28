import boto3
import pandas as pd
import io

#def lambda_handler(event, context):
    # TODO implement
client = boto3.client('s3')  # low-level functional API

# resource = boto3.resource('s3') #high-level object-oriented API
# my_bucket = resource.Bucket('kmbkt') #subsitute this for your s3 bucket name.

obj = client.get_object(Bucket='kiranbkt', Key='data_year_max_temp.csv')
file = obj["Body"].read()
df_yr_temp = pd.read_csv(io.BytesIO(file), delimiter=",", low_memory=False)

print("count: \n{}".format(df_yr_temp.count()))
print("size: {}".format(df_yr_temp.size))
#    return df_yr_temp.to_dict()



#resource = boto3.resource('s3') #high-level object-oriented API
#my_bucket = resource.Bucket('my-bucket') #subsitute this for your s3 bucket name.
#my_bucket.upload_file('file',Key='data_year_max_temp_result.csv')



