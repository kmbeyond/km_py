import pandas as pd
from pandas import DataFrame

'''
1.Create pandas dataframe from string
2.

'''

# string data
result="1.2|1.3|1.5^2.3|2.5|2.6^3.4|3.5|3.9"

rows = result.split('^')
print(rows)
rows = [x for x in rows if x]

df_data = pd.DataFrame(rows, columns=['DATA'])
print(df_data.head())

df_data[["COL1","COL2","COL3"]] = df_data["DATA"].str.split("|", expand=True)
# df_data.drop(['DATA'])
print(df_data.head())

#Operations:
#filter by specific data
WADF = df_data[ df_data['COL1']=='PERFORMANCE_METRICS' ]
WADF = df_data[(df_data['COL1']=='PERFORMANCE_METRICS') & (df_data['city']=='Bellevue')]


dfcust.where( df_data['state']=='WA' ) #BE AWARE: This returns NaN if not match
