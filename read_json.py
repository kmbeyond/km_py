import json

#json string to dict
data = '{"prop":"val"}'
data_json = json.loads(data)
print(data_json['prop'])
print(data_json.get('prop'))

#json from utf-8
payload_str = r'''{"status":{"code":200,"is_success":true}}'''
data = json.loads(payload_str)

#dict/json to string
data_json = json.dumps({ "prop":"val"})
print(data_json)

#From file - expects to be single json
json_path = '/Users/km/km/km_practice/data/read_json_sample.json'
data = json.load(open(json_path))
print(data)

from pathlib import Path
json_path = Path(json_path)
with json_path.open("r", encoding="utf-8") as f:
    data = json.load(f)


#if file data has single quotes (instead of double-quotes); ex:
#{'s3': [{'IpProtocol': 'tcp', 'FromPort': '80', 'ToPort': '80', 'CidrIp': '0.0.0.0/0'}, {'IpProtocol': 'tcp', 'FromPort': '22', 'ToPort': '22', 'CidrIp': '0.0.0.0/0'}]}
json_path = '/Users/km/km/km_practice/data/read_json_sample_single_quotes.json'

import ast
from pathlib import Path
from typing import Any

def read_single_quoted_json(path: str | Path) -> Any:
    text = Path(path).read_text(encoding="utf-8")
    # Works for Python-literal style: {'a': 'b', 'x': [1, 2], 't': True, 'n': None}
    return ast.literal_eval(text)

data = read_single_quoted_json(json_path)
print(data)


print(json.dumps(data, indent=2, sort_keys=True))
sIpProtocol=data["s3"][0]['IpProtocol']
print(sIpProtocol)


#----formatted json doc
print(json.dumps(data))  #flat string
print(json.dumps(data, indent=4))
print(json.dumps(data, indent=2, sort_keys=True))

#----formatted json to file
output_file_readable_json = '/Users/km/km/km_practice/data/read_json_sample_formatted.json'
with open(output_file_readable_json, 'w') as file: file.write(json.dumps(data, indent=4))
with open(output_file_readable_json, 'w') as file: file.write(f"{json.dumps(data, indent=2)}")
