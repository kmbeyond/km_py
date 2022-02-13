import boto3, json

config = {
    "proxy_server": "proxy:port"
}
from botocore.config import Config
proxy_config = Config(
    proxies={
        'http': config['proxy_server'],
        'https': config['proxy_server']
    }
)

dynamodb = boto3.resource(
    service_name="dynamodb",
    region_name="us-east-1"
    #aws_access_key_id=access_key,
    #aws_secret_access_key=secret_key
    #config=proxy_config
)

def km_query_tbl1():
    km_tbl = dynamodb.Table("kmtbl")
    resp = km_tbl.get_item(Key={'applicationId':'inv', 'key':'km_conf'})
    #print(f"resp= {resp}")
    km_conf = json.loads(resp['Item']['value'])
    return {
        "k1": km_conf['k1'],
        "k2": km_conf['k2']
    }


def insert_record():
    km_tbl = dynamodb.Table("kmtbl")
    json_string = '{"applicationId":"inv","execution_id":"1641985460144",...'
    record = json.loads(record)
    #record = {"applicationId":"inv","execution_id":"1641985460144"}
    km_tbl.put_item(Item=record)

    
def strip_values(row):
    return json.loads(row)


def km_query_tbl2():
    table_name = "cdppciprod-ethos-tracking"
    print(f"Connecting to table: {table_name}")
    table = dynamodb.Table(table_name)

    job_id = '4_PPAStageOneUpload'
    import time
    time = time.time()
    d_now = str(round(time * 1000))
    #d_now="1641985460162"
    d_past = str(round((time - (60 * 180)) * 1000))
    #d_past="1641985222111"

    from boto3.dynamodb.conditions import Key
    response = table.query(
        KeyConditionExpression=Key('job_id').eq(job_id) & Key('execution_id').between(d_past, d_now)
    )
    import pandas as pd
    response_df = pd.DataFrame(response['Items'])
    print(f'Query result: {response_df}')

    if response_df.empty:
        print("No records")
    else:
        response_values = response_df['value'].apply(strip_values)
        items_json = response_values.to_json(orient='records')
        items_df = pd.DataFrame.from_dict(json.loads(items_json))

        job = items_df.applymap(lambda x: {} if pd.isnull(x) else x)
        print(job)
        job["flow_name"] = [d.get('flow name') for d in job["metadata"]]
        job["error_message"] = [d.get('error message') for d in job["metadata"]]
        job['executionId'] = job['executionId'].astype(int)
        job.sort_values(by='executionId')



km_query_tbl2()
