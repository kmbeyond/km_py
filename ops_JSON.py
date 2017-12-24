import json


#json data must have data enclosed with double-quotes
json_data = """{"first_name": ["Jason", "Molly", "Tina", "Jake", "Amy"],
        "last_name": ["Miller", "Jacobson", ".", "Milner", "Cooze"],
        "age": [42, 52, 36, 24, 73],
        "preTestScore": [4, 24, 31, ".", "."],
        "postTestScore": ["25,000", "94,000", 57, 62, 70]
        }"""



json_obj = json.loads(json_data)

df=pd.DataFrame(json_obj)

#OR: using DataFrame class from pandas
from pandas import DataFrame
df = DataFrame(json_obj)

#Create DataFrame from specific column(s)
fndf = DataFrame(json_obj['first_name'])
fndf.columns
#RangeIndex(start=0, stop=1, step=1)

fullndf = DataFrame(json_obj['first_name'], json_obj['last_name'])

#read from json file
deptDF = pd.read_json("/home/kiran/km/km_hadoop/data/data_departments.json", lines=True)
deptDF.head(5)
