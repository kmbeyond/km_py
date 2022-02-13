'''
#pre steps

Bucket:
File: km_ingestion/data_year_max_temp.csv
year,max_temp,quality
2001,89,4
2004,85,NA
2002,78,1
2005,88,5
2003,90,4
2009,0,9999
2010,999,4
2011,-4,5

Event=
{
  "bucket_name": "km-bkt",
  "key2": "value2"
}

'''

#resource = boto3.resource('s3')
#my_bucket = resource.Bucket('km-bkt')
#my_bucket.upload_file('/tmp/data_year_max_temp_result.csv', Key='km_ingestion/data_year_max_temp_result.csv')



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
        file_w_prefix = "km_ingestion/data_year_max_temp.csv"
        print(f"File= s3://{bucket_name}/{file_w_prefix}")

        client = boto3.client('s3')  # low-level functional API
        # resource = boto3.resource('s3') #high-level object-oriented API
        # my_bucket = resource.Bucket(bucket_name) #subsitute this for your s3 bucket name.

        obj = client.get_object(Bucket=bucket_name, Key=file_w_prefix)
        file_contents = obj["Body"].read()
        print(f"File contents: {file_contents}")

        #read into pandas df
        df_yr_temp = pd.read_csv(io.BytesIO(file_contents), delimiter=",", low_memory=False)

        print("Top 10 records: \n{}".format(df_yr_temp.head(10)) )
        print("Keys: \n{}".format(df_yr_temp.keys()) )
        print("count: \n{}".format(df_yr_temp.count()) )
        print("size: {}".format(df_yr_temp.size) )

        #df_yr_temp["year"].value_counts()

        def parse_int(x):
            try:
                x = int(x)
            except Exception:
                x = 9999
            return x

        df_yr_temp["quality"] = df_yr_temp["quality"].apply(parse_int)
        print(df_yr_temp.head(5))

        df_yr_max_temp = df_yr_temp.query("quality != 9999").groupby(["year"]).agg({'max_temp' : 'max'}).reset_index()
        print(df_yr_max_temp.head(5))

        resp_data_str = json.loads(json.dumps(df_yr_max_temp.to_json(orient='records')))
        logger.info('ResponseDataSet: {}'.format(resp_data_str))

        response = {
            "statusCode": "200",
            "body": json.loads(json.dumps({
                        "ResponseDataSet": resp_data_str,
                        "input": event
                    })),
            "exception": ""
        }
    except Exception as err:
        response = {
            "statusCode": "400",
            "body": "",
            "exception": str(err)
        }

    return response


print(
lambda_handler({
  "bucket_name": "kiranbkt",
  "key2": "value2"
}, {})
)


