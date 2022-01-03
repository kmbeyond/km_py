
import boto3, json

#key: km_key
#value: abcd<x>efgh<x>ijkl<x>mnop<x>qrst
#sm_key = f"arn:aws:secretsmanager:us-east-1:{aws_account}:secret:km_conf" #no need of arn
sm_key="km_key"
sm_client = boto3.client(service_name="secretsmanager", region_name="us-east-1")
conf_val = sm_client.get_secret_value(SecretId="km_conf")['SecretString']
d_conf_val = json.loads(conf_val)
conf_list = d_conf_val['km_conf'].split('<x>')
km_conf = {'k1':conf_list[0], 'k2':conf_list[1], 'k3':conf_list[2], 'k4':conf_list[3],'k5':conf_list[4]}
