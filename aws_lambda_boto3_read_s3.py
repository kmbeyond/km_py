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

        client = boto3.client('s3')  # low-level functional API

        # resource = boto3.resource('s3') #high-level object-oriented API
        # my_bucket = resource.Bucket('kmbkt') #subsitute this for your s3 bucket name.

        obj = client.get_object(Bucket='kiranbkt', Key='data_year_max_temp.csv')
        file = obj["Body"].read()
        df_yr_temp = pd.read_csv(io.BytesIO(file), delimiter=",", low_memory=False)

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




#resource = boto3.resource('s3') #high-level object-oriented API
#my_bucket = resource.Bucket('my-bucket') #subsitute this for your s3 bucket name.
#my_bucket.upload_file('file',Key='data_year_max_temp_result.csv')



