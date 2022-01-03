import boto3, json

def km_conf():
    dynamodb = boto3.resource("dynamodb")
    km_tbl = dynamodb.Table("kmtbl" )
    resp = km_tbl.get_item(Key={'applicationId':'inv', 'key':'km_conf'})
    #print(f"resp= {resp}")
    km_conf = json.loads(resp['Item']['value'])
    return {
        "k1": km_conf['k1'],
        "k2": km_conf['k2'],
        "k3": km_conf['k3'],
        "k4": km_conf['k4'],
        "k5": km_conf['k5']
    }


km_conf()
