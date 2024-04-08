

import json

input_json_file = 'C:\\km\\json_data_file.json'

json_data = None
with open(input_json_file, 'r') as f:
    data = f.read()
    json_data = json.loads(data)

#print(json.dumps(json_data, indent=4))

output_file_name_json = 'C:\\km\\json_data_file_readable.json'

with open(output_file_name_json, 'w') as file:
    file.write(json.dumps(json_data, indent=4))


#----flatten to column name sep by dot
def flatten_data(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

flat_json = flatten_data(json_data)

print(json.dumps(flat_json, indent=4))


#--json to CSV file
data_list = [(k,v) for k,v in flat_json.items()]
import pandas as pd
df = pd.DataFrame(data_list)
output_file_name = 'C:\\km\\json_data_file.csv'

df.to_csv(output_file_name, header=False, index=True, quoting=1)




