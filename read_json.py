import json

#json string to dict
data = '{"prop":"val"}'
data_json = json.loads(data)
print(data_json['prop'])

#dict/json to string
data_json = json.dumps({ "prop":"val"})
print(data_json)

#From file
#Sample data
#{'s3': [{'IpProtocol': 'tcp', 'FromPort': '80', 'ToPort': '80', 'CidrIp': '0.0.0.0/0'}, {'IpProtocol': 'tcp', 'FromPort': '22', 'ToPort': '22', 'CidrIp': '0.0.0.0/0'}]}
data = json.load(open('read_json_sample.json'))
print(data)

#print(json.dumps(data, indent=2, sort_keys=True))
#sIpProtocol=data["s3"][0]['IpProtocol']
#print(sIpProtocol)


def getData():
    for k, v in data.items():
        for val in v:
            ip_protocol = val['IpProtocol']
            from_port = val['FromPort']
            to_port = val['ToPort']
            cidr_ip = val['CidrIp']
            print("IpProtocol=" + ip_protocol)
            print("FromPort=" + from_port)
            print("ToPort=" + to_port)
            print("CidrIp=" + cidr_ip+"\n")

getData()