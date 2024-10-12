/home/km/km_practice/data/data_fixed_width.txt
0000012024100112560100001230000055.99
0000022024101002331400004510000055.99
0000032024100522863200003780000055.99
0000042024100314562600001170000055.99

import pandas as pd
data_df = pd.read_csv(f"/home/km/km_practice/data/data_fixed_width.txt", delimiter='^', names=['SOURCE_MESSAGE'], header=None)
data_df.head(5)

from datetime import datetime
data_df['ROW_NUMBER'] = data_df.index+1
data_df['JOB_ID'] = '20241011-082233'
data_df['LOAD_DATE'] = datetime.now().strftime('%Y-%m-%d')
data_df['LOAD_TIMESTAMP'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

read_regex = r"(.{6})(.{14})(.{7})(.{10})"
data_columns = ["TXN_ID", "TXN_DATETIME","CUST_NUM","TXN_AMOUNT"]

#data_df['SOURCE_MESSAGE'].str.extractall(read_regex).droplevel(1).head(5)
#data_df2 = data_df['SOURCE_MESSAGE'].str.extractall(read_regex).droplevel(1).set_axis(data_columns, axis=1)

#retain all columns
data_df[data_columns] = data_df['SOURCE_MESSAGE'].str.extractall(read_regex).droplevel(1)
data_df.head(5)

data_df.columns
#Index(['SOURCE_MESSAGE', 'ROW_NUMBER', 'JOB_ID', 'LOAD_DATE', 'LOAD_TIMESTAMP', 'TXN_ID', 'TXN_DATETIME','CUST_NUM', 'TXN_AMOUNT'],dtype='object')

data_df.drop('SOURCE_MESSAGE', axis=1, inplace=True)
data_df.head(5)

