

import json

#----read json file
input_json_file = 'C:\\km\\json_data_file.json'
input_json_file = '/home/km/km/km_practice/data/json_data_file.json'

data = json.load(open(input_json_file))
print(data)

#json_dict = None
with open(input_json_file, 'r') as f: file_data = f.read()
json_dict = json.loads(file_data)


#----formatted json doc
print(json.dumps(json_dict))  #flat string
print(json.dumps(json_dict, indent=4))
print(json.dumps(json_dict, indent=2, sort_keys=True))

#----formatted json to file
output_file_readable_json = '/home/km/km/km_practice/data/json_data_file_readable.json'
with open(output_file_readable_json, 'w') as file: file.write(json.dumps(json_dict, indent=4))
with open(output_file_readable_json, 'w') as file: file.write(f"{json.dumps(data, indent=2)}")


#----flatten to column name sep by dot --> dict of element by dot notation & value
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

for k,v in flat_json.items(): print(f"{k},{v}")

#--write as csv to file
output_file_name = '/home/km/km/km_practice/data/json_data_file_flattened_kv.csv'
with open(output_file_name, 'w') as file:
    for k, v in flat_json.items(): file.write(f"{k}|{v}\n")

#--write as csv to file using pandas
import pandas as pd
data_list = [(k,v) for k,v in flat_json.items()]
df = pd.DataFrame(data_list)
output_file_name = '/home/km/km/km_practice/data/json_data_file_flattened_df.csv'
df.to_csv(output_file_name, header=False, index=True, quoting=1)


#--write as csv to file using function
def flatten_data_to_csv(file, y):
    def flatten( x, name=''):
        if type(x) is dict:
            for a in x: flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:
            #print(f"{name}|{x}")
            file.write(f"{name}|{x}\n")
    flatten(y)

output_file_name = '/home/km/km/km_practice/data/json_data_file_flattened_2.csv'
with open(output_file_name, 'w') as file: 
    flatten_data_to_csv(file, data)


#--flattened json dict to file
output_file_view_json_elements = '/home/km/km/km_practice/data/json_data_file_flattened.json'
with open(output_file_view_json_elements, 'w') as file:
    file.write(f"{json.dumps(flat_json, indent=4)}")

