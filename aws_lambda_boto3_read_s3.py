'''
#pre steps

Bucket:
File: km_data/data_year_max_temp.csv
city,year,quality,max,min
Chicago,2020,9999,90,-20
Chicago,2019,5,85,-40
Chicago,2018,4,84,-32
Chicago,2017,9999,82,-30

Event=
{
  "bucket_name": "km-bkt",
  "key2": "value2"
}

'''

#resource = boto3.resource('s3')
#my_bucket = resource.Bucket('km-bkt')
#my_bucket.upload_file('/tmp/data_year_max_temp_result.csv', Key='km_data/data_year_max_temp_result.csv')



import boto3
import pandas as pd
import io
import json
import logging

def lambda_handler(event, context):
    # TODO implement
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    try:
        bucket_name = "km-bkt"
        bucket_name = event.get('bucket_name')
        file_w_prefix = "km_data/data_year_max_temp.csv"
        client = boto3.client('s3')  # low-level functional API
        # resource = boto3.resource('s3') #high-level object-oriented API
        # my_bucket = resource.Bucket(bucket_name) #subsitute this for your s3 bucket name.

        obj = client.get_object(Bucket=bucket_name, Key=file_w_prefix)
        file_contents = obj["Body"].read()
        print(f"File contents: {file_contents}")
        df_yr_temp = pd.read_csv(io.BytesIO(file_contents), delimiter=",", low_memory=False)

        #print("Top 10 records: \n{}".format(df_yr_temp.head(10)) )
        #print("Keys: \n{}".format(df_yr_temp.keys()) )
        #print("count: \n{}".format(df_yr_temp.count()) )
        #print("size: {}".format(df_yr_temp.size) )

        #df_yr_temp["year"].value_counts()

        def parse_int(x):
            try:
                x = int(x)
            except Exception:
                x = 9999
            return x

        df_yr_temp["quality"] = df_yr_temp["quality"].apply(parse_int)

        df_yr_max_temp = df_yr_temp.query("quality != 9999").groupby(["year"]).agg({'max_temp' : 'max'}).reset_index()

        ResponseDataSetString = json.loads(json.dumps(df_yr_max_temp.to_json(orient='records')))

        logger.info('ResponseDataSet: {}'.format(ResponseDataSetString))
        responseBody = {
            "ResponseDataSet": ResponseDataSetString,
            "input": event
        };
        responseCode = "200"

    except:
        responseCode = "400"
        responseBody = {}

    response = {
        "statusCode": responseCode,
        "headers": {
            "x-custom-header": "my custom header value"
        },
        "body": json.loads(json.dumps(responseBody))
    }

    return response




